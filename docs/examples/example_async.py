import asyncio
import base64
import binascii
import os

# Requires the optional async extra: pip install "py4heappe[async]"
import py4heappe.heappe_v6.core_async as hpa
from py4heappe.heappe_v6.extensions.file_transfer_api_ext_async import (
    FileTransferApiExt,
    InMemoryUploadFile,
)


def load_required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


async def authenticate(api_client: hpa.ApiClient) -> str:
    user_api = hpa.UserAndLimitationManagementApi(api_client)
    return await user_api.heappe_user_and_limitation_management_authenticate_user_password_post(
        authenticate_user_password_model=hpa.AuthenticateUserPasswordModel(
            credentials=hpa.PasswordCredentialsExt(
                username=load_required_env("HEAPPE_USERNAME"),
                password=load_required_env("HEAPPE_PASSWORD"),
            )
        )
    )


async def upload_job_input_from_memory(
    api_client: hpa.ApiClient,
    session_code: str,
) -> None:
    """Optional example: upload one file from base64 env content to an existing job."""
    encoded_content = os.environ.get("HEAPPE_STREAM_UPLOAD_BASE64", "").strip()
    job_id_raw = os.environ.get("HEAPPE_STREAM_UPLOAD_JOB_ID", "").strip()
    if not encoded_content or not job_id_raw:
        print(
            "Skipping in-memory upload (set HEAPPE_STREAM_UPLOAD_BASE64 and "
            "HEAPPE_STREAM_UPLOAD_JOB_ID to enable this example)."
        )
        return

    try:
        file_bytes = base64.b64decode(encoded_content, validate=True)
    except (binascii.Error, ValueError) as exception:
        raise RuntimeError(
            "HEAPPE_STREAM_UPLOAD_BASE64 contains invalid base64 content"
        ) from exception

    filename = os.environ.get("HEAPPE_STREAM_UPLOAD_FILENAME", "").strip() or "input.dat"
    task_id_raw = os.environ.get("HEAPPE_STREAM_UPLOAD_TASK_ID", "").strip()

    stream_api = FileTransferApiExt(api_client)
    await stream_api.heappe_file_transfer_upload_file_objects_to_job_execution_dir_post(
        files=[InMemoryUploadFile(filename=filename, content=file_bytes)],
        session_code=session_code,
        job_id=int(job_id_raw),
        task_id=int(task_id_raw) if task_id_raw else None,
    )
    print(f"Uploaded in-memory file '{filename}' to job {job_id_raw}.")


async def main() -> None:
    configuration = hpa.Configuration(host=load_required_env("HEAPPE_URL"))

    # `async with` closes the underlying aiohttp session when done.
    async with hpa.ApiClient(configuration) as api_client:
        session_code = await authenticate(api_client)
        print("Authenticated.")

        management_api = hpa.ManagementApi(api_client)
        cluster_api = hpa.ClusterInformationApi(api_client)
        job_api = hpa.JobManagementApi(api_client)

        # Independent requests run concurrently on one client.
        version, clusters, jobs = await asyncio.gather(
            management_api.heappe_management_version_information_get(
                session_code=session_code
            ),
            cluster_api.heappe_cluster_information_list_available_clusters_get(
                session_code=session_code
            ),
            job_api.heappe_job_management_list_jobs_for_current_user_get(
                session_code=session_code, limit=10
            ),
        )

        print(f"HEAppE {version.name} {version.version}")
        for cluster in clusters:
            print(f"Cluster {cluster.id}: {cluster.name}")
        for job in jobs:
            state = job.state.value if job.state is not None else None
            print(f"Job {job.id}: {job.name} (state {state})")

        await upload_job_input_from_memory(api_client, session_code)


if __name__ == "__main__":
    asyncio.run(main())
