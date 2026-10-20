from __future__ import absolute_import

import mimetypes

from dataclasses import dataclass
from typing import Any, Optional, Sequence, Tuple, Union, cast

from py4heappe.heappe_v6.core.api.file_transfer_api import FileTransferApi


UploadContent = Union[bytes, bytearray, memoryview, Any]


UploadTuple2 = Tuple[str, UploadContent]
UploadTuple3 = Tuple[str, UploadContent, str]
UploadEntry = Union["InMemoryUploadFile", UploadTuple2, UploadTuple3]


@dataclass
class InMemoryUploadFile:
    """Represents one upload entry for multipart in-memory uploads."""

    filename: str
    content: UploadContent
    content_type: Optional[str] = None


def _read_upload_bytes(content: UploadContent) -> bytes:
    if isinstance(content, (bytes, bytearray, memoryview)):
        return bytes(content)

    if hasattr(content, "read"):
        data = content.read()
        if isinstance(data, str):
            return data.encode("utf-8")
        if isinstance(data, (bytes, bytearray, memoryview)):
            return bytes(data)
        raise TypeError("File-like object .read() must return bytes or str.")

    raise TypeError("Upload content must be bytes-like or a file-like object.")


def _normalize_upload_entry(
    entry: UploadEntry,
) -> InMemoryUploadFile:
    if isinstance(entry, InMemoryUploadFile):
        return entry

    if not isinstance(entry, tuple):
        raise TypeError(
            "Each upload entry must be InMemoryUploadFile or tuple(filename, content[, content_type])."
        )

    if len(entry) == 2:
        tuple_entry = cast(UploadTuple2, entry)
        return InMemoryUploadFile(filename=tuple_entry[0], content=tuple_entry[1])

    if len(entry) == 3:
        tuple_entry = cast(UploadTuple3, entry)
        return InMemoryUploadFile(
            filename=tuple_entry[0],
            content=tuple_entry[1],
            content_type=tuple_entry[2],
        )

    raise TypeError("Upload entry tuple must have 2 or 3 elements.")


class FileTransferApiExt(FileTransferApi):
    """Extension methods for file-transfer workflows not covered by generated API."""

    def heappe_file_transfer_upload_file_objects_to_job_execution_dir_post(
        self,
        files: Sequence[UploadEntry],
        session_code: str,
        job_id: int,
        task_id: Optional[int] = None,
        async_req: Optional[bool] = None,
        _preload_content: bool = True,
        _request_timeout=None,
    ):
        """Upload in-memory content to job execution directory using multipart/form-data."""
        return self.heappe_file_transfer_upload_file_objects_to_job_execution_dir_post_with_http_info(
            files=files,
            session_code=session_code,
            job_id=job_id,
            task_id=task_id,
            async_req=async_req,
            _return_http_data_only=True,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
        )

    def heappe_file_transfer_upload_file_objects_to_job_execution_dir_post_with_http_info(
        self,
        files: Sequence[UploadEntry],
        session_code: str,
        job_id: int,
        task_id: Optional[int] = None,
        async_req: Optional[bool] = None,
        _return_http_data_only: Optional[bool] = None,
        _preload_content: bool = True,
        _request_timeout=None,
    ):
        """Upload bytes or file-like objects to /UploadFilesToJobExecutionDir endpoint."""
        if not files:
            raise ValueError("'files' must contain at least one upload entry.")

        query_params = [("SessionCode", session_code), ("JobId", job_id)]
        if task_id is not None:
            query_params.append(("TaskId", task_id))

        post_params = []
        for entry in files:
            normalized = _normalize_upload_entry(entry)
            if not normalized.filename:
                raise ValueError("Upload filename must not be empty.")

            file_bytes = _read_upload_bytes(normalized.content)
            content_type = (
                normalized.content_type
                or mimetypes.guess_type(normalized.filename)[0]
                or "application/octet-stream"
            )
            post_params.append(
                ("files", (normalized.filename, file_bytes, content_type))
            )

        header_params = {
            "Accept": self.api_client.select_header_accept(["application/json"]),
            "Content-Type": self.api_client.select_header_content_type(
                ["multipart/form-data"]
            ),
        }

        auth_settings = ["Bearer", "ServiceApiKey"]

        return self.api_client.call_api(
            "/heappe/FileTransfer/UploadFilesToJobExecutionDir",
            "POST",
            {},
            query_params,
            header_params,
            body=None,
            post_params=post_params,
            files=None,
            response_type="list[FileUploadResultExt]",
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats={},
        )
