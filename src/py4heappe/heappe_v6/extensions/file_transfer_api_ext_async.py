from typing import Optional, Sequence

from py4heappe.heappe_v6.core_async.api.file_transfer_api import FileTransferApi
from py4heappe.heappe_v6.extensions.file_upload import (
    InMemoryUploadFile,
    UploadEntry,
    _to_multipart_files,
)

__all__ = ["FileTransferApiExt", "InMemoryUploadFile", "UploadEntry"]


class FileTransferApiExt(FileTransferApi):
    """Async extension methods for file-transfer workflows not covered by generated API."""

    async def heappe_file_transfer_upload_file_objects_to_job_execution_dir_post(
        self,
        files: Sequence[UploadEntry],
        session_code: str,
        job_id: int,
        task_id: Optional[int] = None,
        _request_timeout=None,
    ):
        """Upload in-memory content to job execution directory using multipart/form-data."""
        return await self.heappe_file_transfer_upload_files_to_job_execution_dir_post(
            session_code=session_code,
            job_id=job_id,
            task_id=task_id,
            files=_to_multipart_files(files),
            _request_timeout=_request_timeout,
        )

    async def heappe_file_transfer_upload_file_objects_to_job_execution_dir_post_with_http_info(
        self,
        files: Sequence[UploadEntry],
        session_code: str,
        job_id: int,
        task_id: Optional[int] = None,
        _request_timeout=None,
    ):
        """Upload in-memory content and return the full ApiResponse (status, headers, data)."""
        return await self.heappe_file_transfer_upload_files_to_job_execution_dir_post_with_http_info(
            session_code=session_code,
            job_id=job_id,
            task_id=task_id,
            files=_to_multipart_files(files),
            _request_timeout=_request_timeout,
        )

    async def heappe_file_transfer_upload_file_objects_to_job_execution_dir_post_without_preload_content(
        self,
        files: Sequence[UploadEntry],
        session_code: str,
        job_id: int,
        task_id: Optional[int] = None,
        _request_timeout=None,
    ):
        """Upload in-memory content and return the raw, unread REST response."""
        return await self.heappe_file_transfer_upload_files_to_job_execution_dir_post_without_preload_content(
            session_code=session_code,
            job_id=job_id,
            task_id=task_id,
            files=_to_multipart_files(files),
            _request_timeout=_request_timeout,
        )
