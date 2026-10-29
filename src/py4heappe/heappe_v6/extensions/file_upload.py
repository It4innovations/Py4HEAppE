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


def _to_multipart_files(files: Sequence[UploadEntry]) -> List[Tuple[str, bytes]]:
    if not files:
        raise ValueError("'files' must contain at least one upload entry.")

    # OpenAPI-generated upload supports multipart `files` entries as
    # `(filename, bytes)` tuples.
    multipart_files = []
    for entry in files:
        normalized = _normalize_upload_entry(entry)
        if not normalized.filename:
            raise ValueError("Upload filename must not be empty.")
        file_bytes = _read_upload_bytes(normalized.content)
        multipart_files.append((normalized.filename, file_bytes))

    return multipart_files
