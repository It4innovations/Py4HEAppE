import json
import os
import time
from io import StringIO
from pathlib import Path

import paramiko
from paramiko import SSHClient
from scp import SCPClient

import py4heappe.heappe_v6.core as hp

POLL_INTERVAL_SECONDS = 30
OUTPUT_DIRECTORY = Path("data_transfer/output")


def load_required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def create_private_key(credentials: dict):
    private_key_buffer = StringIO(credentials["PrivateKey"])
    cipher_type = credentials["CipherType"]

    if cipher_type in (1, 2):
        return paramiko.RSAKey.from_private_key(private_key_buffer)
    if cipher_type in (3, 4):
        return paramiko.ECDSAKey.from_private_key(private_key_buffer)
    return paramiko.RSAKey.from_private_key(private_key_buffer)


def wait_for_job_completion(
    job_api: hp.JobManagementApi, session_code: str, job_id: int
) -> int:
    current_info_body = {
        "_preload_content": False,
        "SubmittedJobInfoId": job_id,
        "SessionCode": session_code,
    }

    while True:
        response = job_api.heappe_job_management_current_info_for_job_get(
            **current_info_body
        )
        job_info = json.loads(response.data)
        state = job_info["State"]

        if state == 16:
            print(f"Job {job_id} finished.")
            return state
        if state == 32:
            print(f"Job {job_id} failed.")
            return state
        if state == 64:
            print(f"Job {job_id} was canceled.")
            return state

        print(f"Waiting for job {job_id} to finish... current state: {state}")
        time.sleep(POLL_INTERVAL_SECONDS)


def download_job_outputs(
    file_transfer_api: hp.FileTransferApi,
    session_code: str,
    job_id: int,
) -> list[str]:
    request_transfer_body = {
        "_preload_content": False,
        "body": {
            "SubmittedJobInfoId": job_id,
            "SessionCode": session_code,
        },
    }

    response = file_transfer_api.heappe_file_transfer_request_file_transfer_post(
        **request_transfer_body
    )
    job_transfer = json.loads(response.data)

    changed_files_response = (
        file_transfer_api.heappe_file_transfer_list_changed_files_for_job_get(
            _preload_content=False,
            SessionCode=session_code,
            SubmittedJobInfoId=job_id,
        )
    )
    changed_files = json.loads(changed_files_response.data)
    produced_files = [os.path.normpath(item["FileName"]) for item in changed_files]
    print(f"Files changed during job execution: {produced_files}")

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key = create_private_key(job_transfer["Credentials"])

    try:
        ssh.connect(
            job_transfer["ServerHostname"],
            username=job_transfer["Credentials"]["Username"],
            pkey=private_key,
        )
        base_path = job_transfer["SharedBasepath"]

        with SCPClient(ssh.get_transport()) as scp:
            for file_name in produced_files:
                relative_path = file_name.lstrip("/\\")
                output_path = OUTPUT_DIRECTORY / str(job_id) / relative_path
                output_path.parent.mkdir(parents=True, exist_ok=True)
                scp.get(
                    os.path.join(base_path, relative_path).replace("\\", "/"),
                    str(output_path),
                )
    finally:
        ssh.close()

    close_transfer_body = {
        "_preload_content": False,
        "body": {
            "SubmittedJobInfoId": job_id,
            "PublicKey": job_transfer["Credentials"]["PublicKey"],
            "SessionCode": session_code,
        },
    }
    file_transfer_api.heappe_file_transfer_close_file_transfer_post(
        **close_transfer_body
    )

    return produced_files


def main() -> None:
    configuration = hp.Configuration()
    configuration.host = load_required_env("HEAPPE_URL")

    project_accounting_string = load_required_env("HEAPPE_ACCOUNTING_STRING")
    username = load_required_env("HEAPPE_USERNAME")
    password = load_required_env("HEAPPE_PASSWORD")

    cluster_id = int(os.environ.get("HEAPPE_CLUSTER_ID", "2"))
    file_transfer_method_id = int(os.environ.get("HEAPPE_FILE_TRANSFER_METHOD_ID", "1"))
    cluster_node_type_id = int(os.environ.get("HEAPPE_CLUSTER_NODE_TYPE_ID", "18"))
    command_template_id = int(os.environ.get("HEAPPE_COMMAND_TEMPLATE_ID", "3"))

    api_client = hp.ApiClient(configuration)

    try:
        user_api = hp.UserAndLimitationManagementApi(api_client)
        management_api = hp.ManagementApi(api_client)
        cluster_api = hp.ClusterInformationApi(api_client)
        job_api = hp.JobManagementApi(api_client)
        file_transfer_api = hp.FileTransferApi(api_client)
        reporting_api = hp.JobReportingApi(api_client)

        print(f"Authenticating to HEAppE instance as {username}...")
        auth_response = user_api.heappe_user_and_limitation_management_authenticate_user_password_post(
            _preload_content=False,
            body={
                "Credentials": {
                    "Username": username,
                    "Password": password,
                }
            },
        )
        session_code = json.loads(auth_response.data)
        print(f"Session code: {session_code}")

        print("\nFetching HEAppE version info...")
        version_response = management_api.heappe_management_version_information_get(
            _preload_content=False,
            SessionCode=session_code,
        )
        print(json.dumps(json.loads(version_response.data), indent=2))

        print("\nFetching cluster info...")
        cluster_response = (
            cluster_api.heappe_cluster_information_list_available_clusters_get(
                _preload_content=False,
                SessionCode=session_code,
            )
        )
        print(json.dumps(json.loads(cluster_response.data), indent=2))

        print("\nFetching available computational projects...")
        projects_response = user_api.heappe_user_and_limitation_management_projects_for_current_user_get(
            _preload_content=False,
            SessionCode=session_code,
        )
        projects = json.loads(projects_response.data)
        project = next(
            item["Project"]
            for item in projects
            if item["Project"]["AccountingString"] == project_accounting_string
        )
        print(json.dumps(project, indent=2))

        print("\nCreating job...")
        create_job_response = job_api.heappe_job_management_create_job_post(
            _preload_content=False,
            body={
                "SessionCode": session_code,
                "JobSpecification": {
                    "Name": "job_1",
                    "ClusterId": cluster_id,
                    "FileTransferMethodId": file_transfer_method_id,
                    "ProjectId": project["Id"],
                    "EnvironmentVariables": [],
                    "Tasks": [
                        {
                            "Name": "task_1",
                            "MinCores": 1,
                            "MaxCores": 128,
                            "Priority": 4,
                            "WalltimeLimit": 600,
                            "StandardOutputFile": "stdout",
                            "StandardErrorFile": "stderr",
                            "ProgressFile": "stdprog",
                            "LogFile": "stdlog",
                            "ClusterNodeTypeId": cluster_node_type_id,
                            "CommandTemplateId": command_template_id,
                            "TemplateParameterValues": [
                                {
                                    "CommandParameterIdentifier": "inputParam",
                                    "ParameterValue": "testValue",
                                }
                            ],
                        }
                    ],
                },
            },
        )
        created_job = json.loads(create_job_response.data)
        job_id = created_job["Id"]
        print(f"Job ID: {job_id}")

        print(f"\nSubmitting job {job_id}...")
        job_api.heappe_job_management_submit_job_put(
            _preload_content=False,
            body={
                "CreatedJobInfoId": job_id,
                "SessionCode": session_code,
            },
        )

        print(f"\nWaiting for job {job_id} to finish...")
        wait_for_job_completion(job_api, session_code, job_id)

        print("\nDownloading generated files...")
        produced_files = download_job_outputs(file_transfer_api, session_code, job_id)
        print(", ".join(produced_files) + " fetched")

        print("\nFetching resource usage report...")
        usage_response = (
            reporting_api.heappe_job_reporting_resource_usage_report_for_job_get(
                _preload_content=False,
                SessionCode=session_code,
                JobId=job_id,
            )
        )
        usage_report = json.loads(usage_response.data)
        print(f"Job {job_id} used {usage_report['TotalUsage']} resources.")

    finally:
        api_client.pool.close()
        api_client.pool.join()


if __name__ == "__main__":
    main()
