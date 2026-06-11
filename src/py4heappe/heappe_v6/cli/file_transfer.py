import base64
import binascii
import json
import os
import typer
import paramiko
from scp import SCPClient
from io import StringIO

import py4heappe.heappe_v6.cli.configuration as configuration
import py4heappe.heappe_v6.core.base.utils as utils
import py4heappe.heappe_v6.core as heappeCore

from py4heappe.heappe_v6.core.base import exceptions
from py4heappe.heappe_v6.core import rest
from typing import List, Optional
from typing import Annotated

app = typer.Typer(
    name="HEAppEFileTransferCLI", no_args_is_help=True, pretty_exceptions_short=True
)


def _raise_cli_exception_from_api(exception: rest.ApiException):
    try:
        response_data = json.loads(exception.body)
        raise exceptions.Py4HEAppEAPIException(
            response_data["title"], response_data["detail"], response_data["status"]
        ) from None
    except json.JSONDecodeError:
        raise exceptions.Py4HEAppEException(
            "Link to a HEAppE instance is not set or valid. Please check Conf Init option."
        ) from None


def _raise_cli_exception(exception: Exception):
    if isinstance(exception, exceptions.Py4HEAppEAPIInternalException):
        raise exceptions.Py4HEAppEException(exception.message) from None
    if isinstance(exception, exceptions.Py4HEAppEInternalException):
        raise exceptions.Py4HEAppEException(exception.message) from None
    raise exceptions.Py4HEAppEInternalException(
        f"Other exception: {str(exception)}"
    ) from None


def _print_response(label: str, response_data):
    try:
        payload = json.loads(response_data)
        print(f"\n{label}:\n{json.dumps(payload, indent = 3)}")
    except (json.JSONDecodeError, TypeError):
        if isinstance(response_data, bytes):
            response_data = response_data.decode("utf-8", errors="replace")
        print(f"\n{label}:\n{response_data}")


def _extract_base64_response(response_data) -> str:
    if isinstance(response_data, bytes):
        response_data = response_data.decode("utf-8", errors="replace")

    if isinstance(response_data, str):
        try:
            payload = json.loads(response_data)
            if isinstance(payload, str):
                return payload
        except json.JSONDecodeError:
            return response_data

    raise exceptions.Py4HEAppEInternalException(
        "Unexpected response format for file download."
    ) from None


def _write_base64_file_content(
    content: str, download_file_path: str, fallback_name: str
) -> str:
    try:
        decoded_content = base64.b64decode(content, validate=True)
    except (binascii.Error, ValueError) as exception:
        raise exceptions.Py4HEAppEInternalException(
            f"Unable to decode downloaded file content: {str(exception)}"
        ) from None

    resolved_path = os.path.abspath(download_file_path)
    if os.path.isdir(resolved_path):
        file_name = os.path.basename(fallback_name) or "downloaded_file"
        resolved_path = os.path.join(resolved_path, file_name)

    parent_dir = os.path.dirname(resolved_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    with open(resolved_path, "wb") as file_handle:
        file_handle.write(decoded_content)

    return resolved_path


def _request_transfer_tunnel_credentials(id: int):
    body = {
        "_preload_content": False,
        "body": {
            "SubmittedJobInfoId": id,
            "SessionCode": utils.load_stored_session(),
        },
    }

    response = heappeCore.FileTransferApi(
        configuration.get_api_instance()
    ).heappe_file_transfer_request_file_transfer_post(**body)

    return json.loads(response.data)


def _open_transfer_ssh_client(tunnel_credentials: dict):
    hostname = tunnel_credentials.get("ServerHostname")
    username = tunnel_credentials["Credentials"]["Username"]
    port = tunnel_credentials.get("Port", 22)
    private_key = tunnel_credentials["Credentials"]["PrivateKey"].replace("\r", "")

    key_stream = StringIO(private_key)
    key = paramiko.Ed25519Key.from_private_key(key_stream)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print(f"Connecting to {hostname}...")
    ssh.connect(hostname, port=port, username=username, pkey=key)

    if ssh.get_transport() and ssh.get_transport().is_active():
        print("✅ Connection successful!")
    else:
        print("❌ Connection failed (Transport inactive).")

    return ssh


def _transfer_to_remote(scp: SCPClient, remote_path: str, files=None, directory=None):
    if files:
        scp.put(files, remote_path=remote_path)
        return files
    if directory:
        scp.put(directory, remote_path=remote_path, recursive=True)
        return os.path.abspath(directory)

    utils.print_and_log(
        "File transfer tunnel created. No files or directory were provided."
    )
    return None


def _print_transfer_result(transferred_source):
    if transferred_source is None:
        return

    _print_response("Files/Folder transferred", transferred_source)


def _prompt_transfer_source():
    source = typer.prompt(
        "Enter a file path, directory path, or 'q' to quit",
        default="",
        show_default=False,
    ).strip()

    if source.lower() in {"q", "quit"}:
        return None, None, True
    if not source:
        raise exceptions.Py4HEAppEInternalException("Path must not be empty.") from None
    if os.path.isfile(source):
        return [os.path.abspath(source)], None, False
    if os.path.isdir(source):
        return None, os.path.abspath(source), False

    raise exceptions.Py4HEAppEInternalException(
        f"The specified path does not exist: {source}"
    ) from None


def _load_json_response_payload(response_data):
    if isinstance(response_data, bytes):
        response_data = response_data.decode("utf-8", errors="replace")

    if isinstance(response_data, str):
        try:
            return json.loads(response_data)
        except json.JSONDecodeError as exception:
            raise exceptions.Py4HEAppEInternalException(
                f"Unexpected response format for partial file download: {str(exception)}"
            ) from None

    if isinstance(response_data, list):
        return response_data

    raise exceptions.Py4HEAppEInternalException(
        "Unexpected response format for partial file download."
    ) from None


def _get_partial_download_extension(file_type: int) -> str:
    extension_map = {
        0: ".log",
        1: ".txt",
        2: ".txt",
        3: ".txt",
    }

    if file_type not in extension_map:
        raise exceptions.Py4HEAppEInternalException(
            f"Unsupported FileType value: {file_type}"
        ) from None

    return extension_map[file_type]


def _write_downloaded_partial_files(
    response_data, download_directory_path: str
) -> List[str]:
    payload = _load_json_response_payload(response_data)
    if not isinstance(payload, list):
        raise exceptions.Py4HEAppEInternalException(
            "Expected a list of file parts from partial file download."
        ) from None

    target_directory = os.path.abspath(download_directory_path)
    os.makedirs(target_directory, exist_ok=True)

    written_files = []
    for item in payload:
        relative_path = item.get("RelativePath")
        if not relative_path:
            raise exceptions.Py4HEAppEInternalException(
                "RelativePath is missing in partial file download response."
            ) from None

        file_type = item.get("FileType")
        file_extension = _get_partial_download_extension(file_type)
        file_name = f"{os.path.basename(relative_path)}{file_extension}"
        file_path = os.path.join(target_directory, file_name)

        content = item.get("Content", "")

        mode = "r+" if os.path.exists(file_path) else "w+"
        with open(file_path, mode) as file_handle:
            file_handle.write(content)

        written_files.append(file_path)

    return written_files


def _validate_upload_paths(paths: List[str]) -> List[str]:
    normalized_paths = []

    for path in paths:
        normalized_path = os.path.abspath(path)
        if not os.path.isfile(normalized_path):
            raise exceptions.Py4HEAppEInternalException(
                f"The specified path is not a file or does not exist: {path}"
            ) from None
        normalized_paths.append(normalized_path)

    return normalized_paths


def _parse_task_file_offsets(task_file_offsets: List[str]) -> List[dict]:
    parsed_offsets = []

    for item in task_file_offsets:
        parts = item.split(":", 2)
        if len(parts) != 3:
            raise exceptions.Py4HEAppEInternalException(
                "Each task file offset must use submittedTaskInfoId:fileType:offset format."
            ) from None

        submitted_task_info_id, file_type, offset = parts
        if not submitted_task_info_id.isdigit():
            raise exceptions.Py4HEAppEInternalException(
                f"SubmittedTaskInfoId must be an integer in '{item}'."
            ) from None
        if file_type not in {"0", "1", "2", "3"}:
            raise exceptions.Py4HEAppEInternalException(
                f"FileType must be one of 0, 1, 2, 3 in '{item}'."
            ) from None
        if not offset.lstrip("-").isdigit():
            raise exceptions.Py4HEAppEInternalException(
                f"Offset must be an integer in '{item}'."
            ) from None

        parsed_offsets.append(
            {
                "SubmittedTaskInfoId": int(submitted_task_info_id),
                "FileType": int(file_type),
                "Offset": int(offset),
            }
        )

    return parsed_offsets


def _close_file_transfer(
    submitted_job_info_id: int,
    publicKey: str,
):
    """Close file transfer tunnel"""
    try:
        utils.print_and_log("Closing file transfer tunnel ...")
        body = {
            "_preload_content": False,
            "body": {
                "SubmittedJobInfoId": submitted_job_info_id,
                "PublicKey": publicKey,
                "SessionCode": utils.load_stored_session(),
            },
        }

        response = heappeCore.FileTransferApi(
            configuration.get_api_instance()
        ).heappe_file_transfer_close_file_transfer_post(**body)
        _print_response("State", response.data)

    except rest.ApiException as exception:
        _raise_cli_exception_from_api(exception)
    except Exception as exception:
        _raise_cli_exception(exception)


@app.command(name="Single")
def request_file_transfer(
    id: int = typer.Option(..., help="Id (Submitted HPC job)"),
    taskId: int = typer.Option(
        None,
        help="Send file/folder to the task directory. If omitted, transfers land in the job directory.",
    ),
    files: Annotated[
        Optional[List[str]],
        typer.Option(
            help="Local file paths to transfer; repeat the option for multiple files",
        ),
    ] = None,
    directory: Optional[str] = typer.Option(
        None,
        "--directory",
        help="Path of directory to transfer.",
    ),
):
    """Create file transfer tunnel and upload file(s) or folder"""
    ssh = None
    tunnel_credentials = None

    try:
        utils.print_and_log("Requesting file transfer tunnel ...")

        if files and directory:
            raise exceptions.Py4HEAppEInternalException(
                f"Specify either list of files or directory."
            ) from None

        if files:
            files = _validate_upload_paths(files)

        if directory:
            directory = os.path.abspath(directory)
            if not os.path.isdir(directory):
                raise exceptions.Py4HEAppEInternalException(
                    f"The specified path does not exist or is not a directory: {directory}"
                ) from None

        tunnel_credentials = _request_transfer_tunnel_credentials(id)
        remote_path = (
            f"{tunnel_credentials.get('SharedBasepath', '')}/{taskId}"
            if taskId
            else f"{tunnel_credentials.get('SharedBasepath', '')}"
        )

        ssh = _open_transfer_ssh_client(tunnel_credentials)

        with SCPClient(ssh.get_transport()) as scp:
            transferred_source = _transfer_to_remote(
                scp, remote_path, files=files, directory=directory
            )
        _print_transfer_result(transferred_source)

    except rest.ApiException as exception:
        _raise_cli_exception_from_api(exception)
    except Exception as exception:
        _raise_cli_exception(exception)
    finally:
        if ssh is not None:
            try:
                ssh.close()
            except Exception as e:
                utils.print_and_log(f"Warning: Failed to close SSH client: {e}")

        if tunnel_credentials is not None:
            try:
                _close_file_transfer(
                    submitted_job_info_id=id,
                    publicKey=tunnel_credentials["Credentials"].get("PublicKey"),
                )
            except Exception as e:
                utils.print_and_log(
                    f"Warning: Failed to cleanly close file transfer on server: {e}"
                )


@app.command(name="Interactive")
def request_file_transfer_interactive(
    id: int = typer.Option(..., help="Id (Submitted HPC job)"),
    taskId: int = typer.Option(
        None,
        help="Send file/folder to the task directory. If omitted, transfers land in the job directory.",
    ),
):
    """Create file transfer tunnel and keep uploading files or directories until quit"""
    ssh = None
    tunnel_credentials = None

    try:
        utils.print_and_log("Requesting interactive file transfer tunnel ...")
        tunnel_credentials = _request_transfer_tunnel_credentials(id)
        remote_path = (
            f"{tunnel_credentials.get('SharedBasepath', '')}/{taskId}"
            if taskId
            else f"{tunnel_credentials.get('SharedBasepath', '')}"
        )

        ssh = _open_transfer_ssh_client(tunnel_credentials)

        with SCPClient(ssh.get_transport()) as scp:
            while True:
                try:
                    files, directory, should_quit = _prompt_transfer_source()
                except exceptions.Py4HEAppEInternalException as exception:
                    utils.print_and_log(exception.message)
                    continue

                if should_quit:
                    break

                transferred_source = _transfer_to_remote(
                    scp, remote_path, files=files, directory=directory
                )
                _print_transfer_result(transferred_source)
                print()

    except rest.ApiException as exception:
        _raise_cli_exception_from_api(exception)
    except Exception as exception:
        _raise_cli_exception(exception)
    finally:
        if ssh is not None:
            try:
                ssh.close()
            except Exception as e:
                utils.print_and_log(f"Warning: Failed to close SSH client: {e}")

        if tunnel_credentials is not None:
            try:
                _close_file_transfer(
                    submitted_job_info_id=id,
                    publicKey=tunnel_credentials["Credentials"].get("PublicKey"),
                )
            except Exception as e:
                utils.print_and_log(
                    f"Warning: Failed to cleanly close file transfer on server: {e}"
                )


@app.command(name="Download")
def download_file_from_cluster(
    id: int = typer.Option(..., help="Id (Submitted HPC job)"),
    relativeFilePath: str = typer.Option(..., help="Relative file path on cluster"),
    download_file_path: str = typer.Option(
        None,
        "--download-file-path",
        "--download_file_path",
        help="Path where the decoded file should be written.",
    ),
):
    """Download specific file from cluster"""
    try:
        utils.print_and_log("Downloading file from cluster ...")
        body = {
            "_preload_content": False,
            "body": {
                "SubmittedJobInfoId": id,
                "RelativeFilePath": relativeFilePath,
                "SessionCode": utils.load_stored_session(),
            },
        }

        response = heappeCore.FileTransferApi(
            configuration.get_api_instance()
        ).heappe_file_transfer_download_file_from_cluster_post(**body)

        if download_file_path:
            written_file_path = _write_base64_file_content(
                _extract_base64_response(response.data),
                download_file_path,
                relativeFilePath,
            )
            utils.print_and_log(
                f"\nDownloaded file was written to: {written_file_path}"
            )
        else:
            try:
                file_content = base64.b64decode(response.data).decode("utf-8")
            except Exception:
                file_content = response.data
            _print_response(
                "Downloaded file response",
                file_content,
            )

    except rest.ApiException as exception:
        _raise_cli_exception_from_api(exception)
    except Exception as exception:
        _raise_cli_exception(exception)


@app.command(name="DownloadParts")
def download_parts_of_job_files_from_cluster(
    id: int = typer.Option(..., help="Id (Submitted HPC job)"),
    taskFileOffset: Annotated[
        Optional[List[str]],
        typer.Option(
            help="Task file offsets (submittedTaskInfoId:fileType:offset); repeat the option for multiple taskFileOffsets"
        ),
    ] = None,
    download_directory_path: str = typer.Option(
        None,
        "--download-directory-path",
        "--download_directory_path",
        help="Base directory where downloaded files will be saved to.",
    ),
):
    """Download parts of job files from cluster"""
    try:
        if not taskFileOffset:
            raise exceptions.Py4HEAppEInternalException(
                "At least one task file offset must be provided."
            ) from None

        utils.print_and_log("Retrieving parts of job files from cluster ...")
        body = {
            "_preload_content": False,
            "body": {
                "SubmittedJobInfoId": id,
                "TaskFileOffsets": _parse_task_file_offsets(taskFileOffset),
                "SessionCode": utils.load_stored_session(),
            },
        }

        response = heappeCore.FileTransferApi(
            configuration.get_api_instance()
        ).heappe_file_transfer_download_parts_of_job_files_from_cluster_post(**body)

        if download_directory_path:
            written_files = _write_downloaded_partial_files(
                response.data, download_directory_path
            )
            utils.print_and_log("\nDownloaded files were written to:")
            for file_path in written_files:
                print(file_path)
        else:
            _print_response("File", response.data)

    except rest.ApiException as exception:
        _raise_cli_exception_from_api(exception)
    except Exception as exception:
        _raise_cli_exception(exception)


@app.command(name="ListChanged")
def list_changed_files_for_job(
    id: int = typer.Option(..., help="Id (Submitted HPC job)")
):
    """Get all changed files during job execution"""
    try:
        utils.print_and_log("Listing changed job files ...")
        parameters = {
            "_preload_content": False,
            "SubmittedJobInfoId": id,
            "SessionCode": utils.load_stored_session(),
        }

        response = heappeCore.FileTransferApi(
            configuration.get_api_instance()
        ).heappe_file_transfer_list_changed_files_for_job_get(**parameters)
        _print_response("Changed files", response.data)

    except rest.ApiException as exception:
        _raise_cli_exception_from_api(exception)
    except Exception as exception:
        _raise_cli_exception(exception)


@app.command(name="Stream")
def upload_files_to_job_execution_dir(
    id: int = typer.Option(..., help="Id (Created or submitted HPC job)"),
    taskId: int = typer.Option(None, help="Id (Task)"),
    files: Annotated[
        List[str],
        typer.Option(
            help="Local file paths to upload; repeat the option for multiple files",
        ),
    ] = ...,
):
    """Upload files to job execution directory"""
    try:
        utils.print_and_log("Uploading files to job execution directory ...")
        upload_paths = _validate_upload_paths(files)
        if id and taskId:
            parameters = {
                "_preload_content": False,
                "files": upload_paths,
                "JobId": id,
                "TaskId": taskId,
                "SessionCode": utils.load_stored_session(),
            }
        else:
            parameters = {
                "_preload_content": False,
                "files": upload_paths,
                "JobId": id,
                "SessionCode": utils.load_stored_session(),
            }
        response = heappeCore.FileTransferApi(
            configuration.get_api_instance()
        ).heappe_file_transfer_upload_files_to_job_execution_dir_post(**parameters)
        _print_response("Upload results", response.data)

    except rest.ApiException as exception:
        _raise_cli_exception_from_api(exception)
    except Exception as exception:
        _raise_cli_exception(exception)


if __name__ == "__main__":
    app()
