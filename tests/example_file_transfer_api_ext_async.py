"""Upload in-memory files to a HEAppE job with the async FileTransferApiExt.

Requires the async extra: pip install "py4heappe[async]"

Set these in tests/.env (or export them), then run from the repository root:
    PY4HEAPPE_TEST_URL            HEAppE instance URL
    PY4HEAPPE_TEST_SESSION_CODE   session code (for example from `py4heappe Auth UserPass`)
    PY4HEAPPE_TEST_STREAM_JOB_ID  job to upload into
    PY4HEAPPE_TEST_STREAM_TASK_ID optional, upload into this task's directory

    python tests/example_file_transfer_api_ext_async.py
"""

import asyncio
import io
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Use the local sources in src/ instead of an installed package.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import py4heappe.heappe_v6.core_async as hpa  # noqa: E402
from py4heappe.heappe_v6.extensions.file_transfer_api_ext_async import (  # noqa: E402
    FileTransferApiExt,
    InMemoryUploadFile,
)

load_dotenv(Path(__file__).with_name(".env"))

url = os.environ["PY4HEAPPE_TEST_URL"]
session_code = os.environ["PY4HEAPPE_TEST_SESSION_CODE"]
job_id = int(os.environ["PY4HEAPPE_TEST_STREAM_JOB_ID"])
task_id = int(os.environ["PY4HEAPPE_TEST_STREAM_TASK_ID"]) if os.environ.get("PY4HEAPPE_TEST_STREAM_TASK_ID") else None


async def main():
    configuration = hpa.Configuration(host=url)

    # `async with` closes the underlying aiohttp session when done.
    async with hpa.ApiClient(configuration) as api_client:
        upload_api = FileTransferApiExt(api_client)

        # Each entry is an InMemoryUploadFile or a (filename, content[, content_type]) tuple;
        # content can be bytes or a file-like object.
        results = await upload_api.heappe_file_transfer_upload_file_objects_to_job_execution_dir_post(
            files=[
                InMemoryUploadFile("async_hello.txt", b"Hello from Py4HEAppE (async)"),
                ("async_data.bin", io.BytesIO(b"\x00\x01\x02\x03"), "application/octet-stream"),
                ("async_notes.txt", io.StringIO("Uploaded from a text stream")),
            ],
            session_code=session_code,
            job_id=job_id,
            task_id=task_id,
        )

        for result in results:
            print(f"{result.file_name}: succeeded={result.succeeded}, path={result.path}")


asyncio.run(main())
