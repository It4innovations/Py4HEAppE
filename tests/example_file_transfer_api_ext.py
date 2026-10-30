"""Upload in-memory files to a HEAppE job with the sync FileTransferApiExt.

Set these in tests/.env (or export them), then run from the repository root:
    PY4HEAPPE_TEST_URL            HEAppE instance URL
    PY4HEAPPE_TEST_SESSION_CODE   session code (for example from `py4heappe Auth UserPass`)
    PY4HEAPPE_TEST_STREAM_JOB_ID  job to upload into
    PY4HEAPPE_TEST_STREAM_TASK_ID optional, upload into this task's directory

    python tests/example_file_transfer_api_ext.py
"""

import io
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Use the local sources in src/ instead of an installed package.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import py4heappe.heappe_v6.core as hp  # noqa: E402
from py4heappe.heappe_v6.extensions.file_transfer_api_ext import (  # noqa: E402
    FileTransferApiExt,
    InMemoryUploadFile,
)

load_dotenv(Path(__file__).with_name(".env"))

url = os.environ["PY4HEAPPE_TEST_URL"]
session_code = os.environ["PY4HEAPPE_TEST_SESSION_CODE"]
job_id = int(os.environ["PY4HEAPPE_TEST_STREAM_JOB_ID"])
task_id = int(os.environ["PY4HEAPPE_TEST_STREAM_TASK_ID"]) if os.environ.get("PY4HEAPPE_TEST_STREAM_TASK_ID") else None

configuration = hp.Configuration()
configuration.host = url
api_client = hp.ApiClient(configuration)

upload_api = FileTransferApiExt(api_client)

# Each entry is an InMemoryUploadFile or a (filename, content[, content_type]) tuple;
# content can be bytes or a file-like object.
results = upload_api.heappe_file_transfer_upload_file_objects_to_job_execution_dir_post(
    files=[
        InMemoryUploadFile("hello.txt", b"Hello from Py4HEAppE (sync)"),
        ("data.bin", io.BytesIO(b"\x00\x01\x02\x03"), "application/octet-stream"),
        ("notes.txt", io.StringIO("Uploaded from a text stream")),
    ],
    session_code=session_code,
    job_id=job_id,
    task_id=task_id,
)

for result in results:
    print(f"{result.file_name}: succeeded={result.succeeded}, path={result.path}")
