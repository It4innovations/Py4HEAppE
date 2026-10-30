from typing import Optional, Sequence

from py4heappe.heappe_v6.core.api.file_transfer_api import FileTransferApi
from py4heappe.heappe_v6.extensions.file_upload import (
    InMemoryUploadFile,
    UploadEntry,
    _to_multipart_files,
)

__all__ = ["FileTransferApiExt", "InMemoryUploadFile", "UploadEntry"]


class FileTransferApiExt(FileTransferApi):
    """Extension methods for file-transfer workflows not covered by generated API."""

    def heappe_file_transfer_upload_file_objects_to_job_execution_dir_post(
        self,
        files: Sequence[UploadEntry],
        session_code: str,
        job_id: int,
        task_id: Optional[int] = None,
        _preload_content: bool = True,
        _request_timeout=None,
    ):
        """Upload in-memory content to job execution directory using multipart/form-data."""
        return self.heappe_file_transfer_upload_file_objects_to_job_execution_dir_post_with_http_info(
            files=files,
            session_code=session_code,
            job_id=job_id,
            task_id=task_id,
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
        _return_http_data_only: Optional[bool] = None,
        _preload_content: bool = True,
        _request_timeout=None,
    ):
        """Upload bytes or file-like objects to /UploadFilesToJobExecutionDir endpoint."""
        # Keep legacy extension input API and map it to generated multipart args.
        multipart_files = _to_multipart_files(files)

        if _preload_content:
            return self.heappe_file_transfer_upload_files_to_job_execution_dir_post(
                session_code=session_code,
                job_id=job_id,
                task_id=task_id,
                files=multipart_files,
                _request_timeout=_request_timeout,
            )

        return self.heappe_file_transfer_upload_files_to_job_execution_dir_post_without_preload_content(
            session_code=session_code,
            job_id=job_id,
            task_id=task_id,
            files=multipart_files,
            _request_timeout=_request_timeout,
        )
