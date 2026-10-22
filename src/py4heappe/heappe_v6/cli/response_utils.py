import json
import os
from typing import Any

import py4heappe.heappe_v6.core.base.utils as utils
from py4heappe.heappe_v6.core.base import exceptions


def _is_env_flag_enabled(env_var_name: str) -> bool:
    return os.environ.get(env_var_name, "").strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
    }


def parse_response_payload(
    response: Any,
    *,
    debug_env_var: str | None = None,
    debug_context: str = "Response",
) -> Any:
    raw_payload = getattr(response, "data", response)

    if debug_env_var and _is_env_flag_enabled(debug_env_var):
        utils.print_and_log(
            f"{debug_context} raw payload type={type(raw_payload).__name__}, value={raw_payload!r}"
        )

    if isinstance(raw_payload, (bytes, bytearray)):
        try:
            payload = json.loads(raw_payload.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            raise exceptions.Py4HEAppEInternalException(
                f"{debug_context} payload is not valid UTF-8 JSON text."
            ) from None
    elif isinstance(raw_payload, str):
        try:
            payload = json.loads(raw_payload)
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEInternalException(
                f"{debug_context} payload is not valid JSON text."
            ) from None
    else:
        payload = raw_payload

    if debug_env_var and _is_env_flag_enabled(debug_env_var):
        utils.print_and_log(
            f"{debug_context} parsed payload type={type(payload).__name__}, value={payload!r}"
        )

    return payload


def extract_first_value(payload: Any, *keys: str) -> Any:
    if not isinstance(payload, dict):
        raise exceptions.Py4HEAppEInternalException(
            "Unexpected response payload type: "
            f"{type(payload).__name__}. Response payload: {payload}"
        ) from None

    for key in keys:
        if key in payload:
            return payload[key]

    raise exceptions.Py4HEAppEInternalException(
        f"Expected one of keys {keys} in response payload. "
        f"Response payload: {payload}"
    ) from None


def extract_id(payload: Any) -> Any:
    if isinstance(payload, int):
        return payload

    if isinstance(payload, dict):
        return extract_first_value(
            payload,
            "Id",
            "id",
            "CreatedJobInfoId",
            "createdJobInfoId",
            "CommandTemplateId",
            "commandTemplateId",
            "CommandTemplateParameterId",
            "commandTemplateParameterId",
        )

    raise exceptions.Py4HEAppEInternalException(
        f"Unexpected response payload for ID extraction: {payload}"
    ) from None

