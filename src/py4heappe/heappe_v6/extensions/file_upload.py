import asyncio
import inspect
from dataclasses import dataclass
from typing import Any, List, Optional, Sequence, Tuple, Union, cast


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


def _read_data_to_bytes(data: Any) -> bytes:
    if isinstance(data, str):
        return data.encode("utf-8")
    if isinstance(data, (bytes, bytearray, memoryview)):
        return bytes(data)
    raise TypeError("File-like object .read() must return bytes or str.")


def _read_upload_bytes(content: UploadContent) -> bytes:
    if isinstance(content, (bytes, bytearray, memoryview)):
        return bytes(content)

    if hasattr(content, "read"):
        return _read_data_to_bytes(content.read())

    raise TypeError("Upload content must be bytes-like or a file-like object.")


async def _read_upload_bytes_async(content: UploadContent) -> bytes:
    if isinstance(content, (bytes, bytearray, memoryview)):
        return bytes(content)

    if hasattr(content, "read"):
        # Async file objects (e.g. aiofiles handles) are awaited directly. A regular
        # file-like .read() is blocking I/O, so it runs in a worker thread to keep the
        # event loop free; if it hands back an awaitable, that is awaited here.
        if inspect.iscoroutinefunction(content.read):
            data = await content.read()
        else:
            data = await asyncio.to_thread(content.read)
            if inspect.isawaitable(data):
                data = await data
        return _read_data_to_bytes(data)

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


def _normalize_upload_entries(files: Sequence[UploadEntry]) -> List[InMemoryUploadFile]:
    if not files:
        raise ValueError("'files' must contain at least one upload entry.")

    normalized_entries = []
    for entry in files:
        normalized = _normalize_upload_entry(entry)
        if not normalized.filename:
            raise ValueError("Upload filename must not be empty.")
        normalized_entries.append(normalized)

    return normalized_entries


# OpenAPI-generated upload supports multipart `files` entries as
# `(filename, bytes)` tuples.
def _to_multipart_files(files: Sequence[UploadEntry]) -> List[Tuple[str, bytes]]:
    return [
        (entry.filename, _read_upload_bytes(entry.content))
        for entry in _normalize_upload_entries(files)
    ]


async def _to_multipart_files_async(files: Sequence[UploadEntry]) -> List[Tuple[str, bytes]]:
    return [
        (entry.filename, await _read_upload_bytes_async(entry.content))
        for entry in _normalize_upload_entries(files)
    ]
