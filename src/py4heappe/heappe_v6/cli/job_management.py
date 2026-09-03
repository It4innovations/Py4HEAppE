import json
from copy import deepcopy
from pathlib import Path
import typer

import py4heappe.heappe_v6.cli.configuration as configuration
import py4heappe.heappe_v6.core.base.utils as utils
import py4heappe.heappe_v6.cli.information as infoCLI
import py4heappe.heappe_v6.core as heappeCore

from py4heappe.heappe_v6.core.base import exceptions
from py4heappe.heappe_v6.core import rest

from typing import Any, Callable, List, Optional
from typing_extensions import Annotated

app = typer.Typer(
    name="HEAppEJobManagementCLI", no_args_is_help=True, pretty_exceptions_short=True
)


MINIMAL_JOB_SPECIFICATION_TEMPLATE = {
    "SessionCode": "",
    "JobSpecification": {
        "Name": "test",
        "ClusterId": 1,
        "FileTransferMethodId": 1,
        "IsExtraLong": False,
        "Tasks": [
            {
                "Name": "test1",
                "MinCores": 1,
                "MaxCores": 1,
                "WalltimeLimit": 900,
                "StandardOutputFile": "stdout",
                "StandardErrorFile": "stderr",
                "ProgressFile": "stdprog",
                "LogFile": "stdlog",
                "ClusterNodeTypeId": 1,
                "CommandTemplateId": 1,
                "TemplateParameterValues": [
                    {
                        "CommandParameterIdentifier": "inputParam",
                        "ParameterValue": "test",
                    }
                ],
            }
        ],
        "ProjectId": 1,
    },
}

FULL_JOB_SPECIFICATION_TEMPLATE = {
    "SessionCode": "string",
    "JobSpecification": {
        "Name": "string",
        "ProjectId": 0,
        "SubProjectIdentifier": "string",
        "WaitingLimit": 0,
        "NotificationEmail": "string",
        "PhoneNumber": "string",
        "NotifyOnAbort": True,
        "NotifyOnFinish": True,
        "NotifyOnStart": True,
        "ClusterId": 0,
        "FileTransferMethodId": 0,
        "Reservation": "string",
        "IsExtraLong": True,
        "EnvironmentVariables": [
            {
                "Name": "string",
                "Value": "string",
            }
        ],
        "Tasks": [
            {
                "Name": "string",
                "MinCores": 0,
                "MaxCores": 0,
                "GpuCores": 0,
                "GpuNodes": 0,
                "WalltimeLimit": 0,
                "PlacementPolicy": "string",
                "Priority": 0,
                "JobArrays": "string",
                "IsExclusive": True,
                "IsRerunnable": True,
                "StandardInputFile": "string",
                "StandardOutputFile": "string",
                "StandardErrorFile": "string",
                "ProgressFile": "string",
                "LogFile": "string",
                "ClusterTaskSubdirectory": "string",
                "ClusterNodeTypeId": 0,
                "CommandTemplateId": 0,
                "CpuHyperThreading": True,
                "RequiredNodes": ["string"],
                "TaskParallelizationParameters": [
                    {
                        "MPIProcesses": 0,
                        "OpenMPThreads": 0,
                        "MaxCores": 0,
                    }
                ],
                "EnvironmentVariables": [
                    {
                        "Name": "string",
                        "Value": "string",
                    }
                ],
                "Memory": 0,
                "MemoryPerCPU": 0,
                "MemoryPerGPU": 0,
                "DependsOn": ["string"],
                "TemplateParameterValues": [
                    {
                        "CommandParameterIdentifier": "string",
                        "ParameterValue": "string",
                    }
                ],
            }
        ],
    },
}

DEFAULT_RESULT_JOB_SPECIFICATION_FILENAME = "resultJobSpecJson.json"

DEFAULT_CREATE_JOB_SPECIFICATION = {
    "SessionCode": "",
    "JobSpecification": {
        "WaitingLimit": 0,
        "FileTransferMethodId": 3,
        "IsExtraLong": False,
        "Tasks": [
            {
                "MinCores": 1,
                "StandardOutputFile": "stdout",
                "StandardErrorFile": "stderr",
                "ProgressFile": "stdprog",
                "LogFile": "stdlog",
            }
        ],
    },
}

TASK_PRIORITY_ALLOWED_VALUES = {
    value
    for name, value in vars(heappeCore.TaskPriorityExt).items()
    if name.startswith("_") and name[1:].isdigit()
}

PRIMITIVE_SWAGGER_TYPE_CONVERTERS = {
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
}


def _parse_bool_string(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"true", "1", "yes", "y", "on"}:
        return True
    if normalized in {"false", "0", "no", "n", "off"}:
        return False
    raise exceptions.Py4HEAppEInternalException(
        f'Boolean value "{value}" is not valid.'
    ) from None


def _convert_override_value(
    raw_value: str, converter: Callable[[str], Any], option_name: str
) -> Any:
    try:
        if converter is bool:
            return _parse_bool_string(raw_value)
        return converter(raw_value)
    except exceptions.Py4HEAppEInternalException:
        raise
    except ValueError:
        raise exceptions.Py4HEAppEInternalException(
            f'Value "{raw_value}" is not valid for {option_name}.'
        ) from None


def _get_swagger_type_converter(
    swagger_type: str, option_name: str
) -> Optional[Callable[[str], Any]]:
    if swagger_type in PRIMITIVE_SWAGGER_TYPE_CONVERTERS:
        return PRIMITIVE_SWAGGER_TYPE_CONVERTERS[swagger_type]

    if swagger_type == "TaskPriorityExt":
        return lambda raw_value: _normalize_task_priority_value(raw_value, option_name)

    return None


def _get_model_field_converters(model_class: type, option_name: str) -> dict:
    field_converters = {}
    for attribute_name, swagger_type in model_class.swagger_types.items():
        json_field_name = model_class.attribute_map[attribute_name]
        converter = _get_swagger_type_converter(swagger_type, option_name)
        if converter is not None:
            field_converters[json_field_name] = converter

    return field_converters


def _normalize_task_priority_value(value: Any, option_name: str) -> str:
    normalized_value = str(value)
    if normalized_value not in TASK_PRIORITY_ALLOWED_VALUES:
        raise exceptions.Py4HEAppEInternalException(
            f'Value "{value}" is not valid for {option_name}.'
        ) from None

    return normalized_value


def _parse_non_negative_index(raw_value: str, option_name: str) -> int:
    try:
        parsed_index = int(raw_value)
    except ValueError:
        raise exceptions.Py4HEAppEInternalException(
            f'Index "{raw_value}" is not valid for {option_name}.'
        ) from None

    if parsed_index < 0:
        raise exceptions.Py4HEAppEInternalException(
            f'Index "{raw_value}" is not valid for {option_name}.'
        ) from None

    return parsed_index


def _ensure_object_list_item(items: List[Any], index: int) -> dict:
    while len(items) <= index:
        items.append({})

    if not isinstance(items[index], dict):
        items[index] = {}

    return items[index]


def _ensure_scalar_list_size(items: List[Any], index: int) -> None:
    while len(items) <= index:
        items.append(None)


def _deep_merge_dicts(base: Any, override: Any) -> Any:
    if isinstance(base, dict) and isinstance(override, dict):
        merged = deepcopy(base)
        for key, value in override.items():
            if key in merged:
                merged[key] = _deep_merge_dicts(merged[key], value)
            else:
                merged[key] = deepcopy(value)
        return merged

    return deepcopy(override)


def _load_job_specification_file(json_job_spec_file: Path) -> dict:
    file_path = json_job_spec_file.expanduser()
    if not file_path.is_file():
        raise exceptions.Py4HEAppEInternalException(
            f"Job specification file does not exist: {file_path}"
        ) from None

    try:
        with file_path.open("r", encoding="utf-8") as input_file:
            loaded_specification = json.load(input_file)
    except json.JSONDecodeError as exception:
        raise exceptions.Py4HEAppEInternalException(
            f"Job specification file is not valid JSON: {file_path}"
        ) from None
    except OSError as exception:
        raise exceptions.Py4HEAppEInternalException(
            f"Job specification file cannot be read: {file_path}"
        ) from None

    if not isinstance(loaded_specification, dict):
        raise exceptions.Py4HEAppEInternalException(
            "Job specification JSON root must be an object."
        ) from None

    return loaded_specification


def _deserialize_generated_model(data: dict, model_class: type) -> Any:
    api_client = heappeCore.ApiClient()
    try:
        return api_client._ApiClient__deserialize_model(data, model_class)
    finally:
        api_client.pool.close()
        api_client.pool.join()


def _normalize_task_specification_data(task_specification: dict) -> None:
    priority = task_specification.get("Priority")
    if priority is not None:
        task_specification["Priority"] = _normalize_task_priority_value(
            priority, "Priority"
        )

    depends_on = task_specification.get("DependsOn")
    if not depends_on:
        return

    normalized_dependencies = []
    for dependency in depends_on:
        if isinstance(dependency, str):
            normalized_dependency = {"Name": dependency}
        elif isinstance(dependency, dict):
            normalized_dependency = deepcopy(dependency)
        else:
            raise exceptions.Py4HEAppEInternalException(
                "Each DependsOn item must be a task name or a task object."
            ) from None

        _normalize_task_specification_data(normalized_dependency)
        normalized_dependencies.append(normalized_dependency)

    task_specification["DependsOn"] = normalized_dependencies


def _build_create_job_model(
    parsed_specification: dict,
) -> heappeCore.CreateJobByProjectModel:
    model_data = deepcopy(parsed_specification)
    tasks = model_data.get("JobSpecification", {}).get("Tasks", [])
    for task in tasks:
        _normalize_task_specification_data(task)

    return _deserialize_generated_model(model_data, heappeCore.CreateJobByProjectModel)


def _apply_object_list_overrides(
    target: dict,
    list_key: str,
    entries: Optional[List[str]],
    model_class: type,
    option_name: str,
) -> None:
    if not entries:
        return

    field_types = _get_model_field_converters(model_class, option_name)
    objects = target.setdefault(list_key, [])
    for entry in entries:
        parts = entry.split(":", 2)
        if len(parts) != 3:
            raise exceptions.Py4HEAppEInternalException(
                f"{option_name} must use index:field:value format."
            ) from None

        item_index = _parse_non_negative_index(parts[0], option_name)
        field_name = parts[1]
        if field_name not in field_types:
            raise exceptions.Py4HEAppEInternalException(
                f'Field "{field_name}" is not supported for {option_name}.'
            ) from None

        item = _ensure_object_list_item(objects, item_index)
        item[field_name] = _convert_override_value(
            parts[2], field_types[field_name], option_name
        )


def _apply_task_scalar_overrides(
    tasks: List[Any],
    entries: Optional[List[str]],
    field_name: str,
    converter: Callable[[str], Any],
    option_name: str,
) -> None:
    if not entries:
        return

    for entry in entries:
        parts = entry.split(":", 1)
        if len(parts) == 1:
            task_index = 0
            raw_value = parts[0]
        elif len(parts) == 2:
            task_index = _parse_non_negative_index(parts[0], option_name)
            raw_value = parts[1]
        else:
            raise exceptions.Py4HEAppEInternalException(
                f"{option_name} must use taskIndex:value format."
            ) from None

        task = _ensure_object_list_item(tasks, task_index)
        task[field_name] = _convert_override_value(raw_value, converter, option_name)


def _apply_task_scalar_list_overrides(
    tasks: List[Any],
    entries: Optional[List[str]],
    list_key: str,
    converter: Callable[[str], Any],
    option_name: str,
) -> None:
    if not entries:
        return

    for entry in entries:
        parts = entry.split(":", 2)
        if len(parts) != 3:
            raise exceptions.Py4HEAppEInternalException(
                f"{option_name} must use taskIndex:itemIndex:value format."
            ) from None

        task_index = _parse_non_negative_index(parts[0], option_name)
        item_index = _parse_non_negative_index(parts[1], option_name)
        task = _ensure_object_list_item(tasks, task_index)
        scalar_values = task.setdefault(list_key, [])
        _ensure_scalar_list_size(scalar_values, item_index)
        scalar_values[item_index] = _convert_override_value(
            parts[2], converter, option_name
        )


def _apply_task_object_list_overrides(
    tasks: List[Any],
    entries: Optional[List[str]],
    list_key: str,
    model_class: type,
    option_name: str,
) -> None:
    if not entries:
        return

    field_types = _get_model_field_converters(model_class, option_name)
    for entry in entries:
        parts = entry.split(":", 3)
        if len(parts) != 4:
            raise exceptions.Py4HEAppEInternalException(
                (f"{option_name} must use " "taskIndex:itemIndex:field:value format.")
            ) from None

        task_index = _parse_non_negative_index(parts[0], option_name)
        item_index = _parse_non_negative_index(parts[1], option_name)
        field_name = parts[2]
        if field_name not in field_types:
            raise exceptions.Py4HEAppEInternalException(
                f'Field "{field_name}" is not supported for {option_name}.'
            ) from None

        task = _ensure_object_list_item(tasks, task_index)
        objects = task.setdefault(list_key, [])
        item = _ensure_object_list_item(objects, item_index)
        item[field_name] = _convert_override_value(
            parts[3], field_types[field_name], option_name
        )


def _parse_cmd_template_parameters(
    parameters: Optional[List[str]],
) -> Optional[List[dict]]:
    if not parameters:
        return None

    parsed_parameters = []
    for parameter in parameters:
        if ":" not in parameter:
            raise exceptions.Py4HEAppEInternalException(
                "Each parameter must be in key:value format with non-empty key and value."
            ) from None

        key, value = parameter.split(":", 1)
        if not key or not value:
            raise exceptions.Py4HEAppEInternalException(
                "Each parameter must be in key:value format with non-empty key and value."
            ) from None

        parsed_parameters.append(
            {
                "CommandParameterIdentifier": key,
                "ParameterValue": value,
            }
        )

    return parsed_parameters


def _normalize_job_specification(parsed_specification: dict) -> dict:
    job_specification = parsed_specification.setdefault("JobSpecification", {})

    for key, value in DEFAULT_CREATE_JOB_SPECIFICATION["JobSpecification"].items():
        if key == "Tasks":
            continue
        job_specification.setdefault(key, deepcopy(value))

    tasks = job_specification.setdefault("Tasks", [])
    if not tasks:
        tasks.append(
            deepcopy(DEFAULT_CREATE_JOB_SPECIFICATION["JobSpecification"]["Tasks"][0])
        )

    default_task = DEFAULT_CREATE_JOB_SPECIFICATION["JobSpecification"]["Tasks"][0]
    for task in tasks:
        if not isinstance(task, dict):
            raise exceptions.Py4HEAppEInternalException(
                "Each task definition must be a JSON object."
            ) from None
        for key, value in default_task.items():
            task.setdefault(key, deepcopy(value))

    if not parsed_specification.get("SessionCode"):
        parsed_specification["SessionCode"] = utils.load_stored_session()

    if not job_specification.get("ProjectId"):
        job_specification["ProjectId"] = infoCLI.get_hpc_project()["Id"]

    if job_specification.get("Name") and not tasks[0].get("Name"):
        tasks[0]["Name"] = job_specification["Name"]

    if tasks[0].get("Name") and not job_specification.get("Name"):
        job_specification["Name"] = tasks[0]["Name"]

    return parsed_specification


def _validate_required_job_specification_fields(parsed_specification: dict) -> None:
    job_specification = parsed_specification.get("JobSpecification", {})
    tasks = job_specification.get("Tasks", [])

    missing_fields = []
    if not parsed_specification.get("SessionCode"):
        missing_fields.append("SessionCode")
    if not job_specification.get("Name"):
        missing_fields.append("JobSpecification.Name")
    if not job_specification.get("ProjectId"):
        missing_fields.append("JobSpecification.ProjectId")
    if not job_specification.get("ClusterId"):
        missing_fields.append("JobSpecification.ClusterId")
    if not job_specification.get("FileTransferMethodId"):
        missing_fields.append("JobSpecification.FileTransferMethodId")
    if not tasks:
        missing_fields.append("JobSpecification.Tasks[0]")
    else:
        first_task = tasks[0]
        required_task_fields = [
            "Name",
            "MinCores",
            "MaxCores",
            "WalltimeLimit",
            "ClusterNodeTypeId",
            "CommandTemplateId",
        ]
        for field_name in required_task_fields:
            if not first_task.get(field_name):
                missing_fields.append(f"JobSpecification.Tasks[0].{field_name}")

    if missing_fields:
        raise exceptions.Py4HEAppEInternalException(
            "The job specification is missing required values: "
            + ", ".join(missing_fields)
        ) from None


def parse_job_specification(
    json_job_spec_file: Optional[Path],
    job_overrides: dict,
    task_scalar_overrides: dict,
    job_environment_variables: Optional[List[str]],
    task_required_nodes: Optional[List[str]],
    task_depends_on: Optional[List[str]],
    task_parallelization_parameters: Optional[List[str]],
    task_environment_variables: Optional[List[str]],
    task_template_parameter_values: Optional[List[str]],
    cmd_template_parameters: Optional[List[str]],
) -> heappeCore.CreateJobByProjectModel:
    parsed_specification = deepcopy(DEFAULT_CREATE_JOB_SPECIFICATION)

    if json_job_spec_file:
        parsed_specification = _deep_merge_dicts(
            parsed_specification,
            _load_job_specification_file(json_job_spec_file),
        )

    job_specification = parsed_specification.setdefault("JobSpecification", {})
    tasks = job_specification.setdefault("Tasks", [])

    for field_name, field_value in job_overrides.items():
        if field_value is None:
            continue
        if field_name == "SessionCode":
            parsed_specification[field_name] = field_value
        else:
            job_specification[field_name] = field_value

    _apply_object_list_overrides(
        job_specification,
        "EnvironmentVariables",
        job_environment_variables,
        heappeCore.EnvironmentVariableExt,
        "--job-environment-variable",
    )

    parsed_template_parameters = _parse_cmd_template_parameters(cmd_template_parameters)
    if parsed_template_parameters is not None:
        task = _ensure_object_list_item(tasks, 0)
        task["TemplateParameterValues"] = parsed_template_parameters

    for field_name, override_definition in task_scalar_overrides.items():
        entries, converter, option_name = override_definition
        _apply_task_scalar_overrides(tasks, entries, field_name, converter, option_name)

    _apply_task_scalar_list_overrides(
        tasks,
        task_required_nodes,
        "RequiredNodes",
        str,
        "--task-required-node",
    )
    _apply_task_scalar_list_overrides(
        tasks,
        task_parallelization_parameters,
        "TaskParallelizationParameters",
        heappeCore.TaskParalizationParameterExt,
        "--task-parallelization-parameter",
    )
    _apply_task_object_list_overrides(
        tasks,
        task_environment_variables,
        "EnvironmentVariables",
        heappeCore.EnvironmentVariableExt,
        "--task-environment-variable",
    )
    _apply_task_object_list_overrides(
        tasks,
        task_template_parameter_values,
        "TemplateParameterValues",
        heappeCore.CommandTemplateParameterValueExt,
        "--task-template-parameter-value",
    )
    _apply_task_object_list_overrides(
        tasks,
        task_depends_on,
        "DependsOn",
        heappeCore.TaskSpecificationExt,
        "--task-depends-on",
    )

    parsed_specification = _normalize_job_specification(parsed_specification)
    _validate_required_job_specification_fields(parsed_specification)
    return _build_create_job_model(parsed_specification)


@app.command(name="InitJobSpecification")
def init_job_specification(
    file_destination: Optional[str] = typer.Option(
        None,
        help="Destination directory or JSON file path for the initialized job specification.",
    ),
    full: bool = typer.Option(
        False,
        "--full/--minimal",
        help="Initialize a full job specification instead of the default minimal template.",
    ),
):
    """Create a minimal or full HPC job specification JSON file."""
    try:
        job_specification = deepcopy(
            FULL_JOB_SPECIFICATION_TEMPLATE
            if full
            else MINIMAL_JOB_SPECIFICATION_TEMPLATE
        )

        destination = (
            Path(file_destination).expanduser() if file_destination else Path.cwd()
        )
        if destination.suffix.lower() == ".json":
            file_path = destination
            file_path.parent.mkdir(parents=True, exist_ok=True)
        else:
            destination.mkdir(parents=True, exist_ok=True)
            file_path = destination / "job_specification.json"

        file_path.write_text(json.dumps(job_specification, indent=4), encoding="utf-8")
        utils.print_and_log(
            f"{'Full' if full else 'Minimal'} job specification was created in: {file_path.resolve()}"
        )

    except exceptions.Py4HEAppEInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except Exception as exception:
        raise exceptions.Py4HEAppEInternalException(
            f"Other exception: {str(exception)}"
        ) from None


@app.command(name="Create")
def create_job(
    json_job_spec_file: Optional[Path] = typer.Option(
        None,
        "--json-job-spec-file",
        help="Path to a JSON job specification file.",
    ),
    session_code: Optional[str] = typer.Option(
        None, "--session-code", help="Session code."
    ),
    name: Optional[str] = typer.Option(None, "--name", help="Name of the HPC job."),
    project_id: Optional[int] = typer.Option(
        None, "--project-id", help="Project identifier."
    ),
    sub_project_identifier: Optional[str] = typer.Option(
        None,
        "--sub-project-identifier",
        help="Sub-project identifier.",
    ),
    waiting_limit: Optional[int] = typer.Option(
        None, "--waiting-limit", help="Waiting limit in seconds."
    ),
    notification_email: Optional[str] = typer.Option(
        None, "--notification-email", help="Notification email address."
    ),
    phone_number: Optional[str] = typer.Option(
        None, "--phone-number", help="Notification phone number."
    ),
    notify_on_abort: Optional[bool] = typer.Option(
        None,
        "--notify-on-abort/--no-notify-on-abort",
        help="Enable or disable notification on abort.",
    ),
    notify_on_finish: Optional[bool] = typer.Option(
        None,
        "--notify-on-finish/--no-notify-on-finish",
        help="Enable or disable notification on finish.",
    ),
    notify_on_start: Optional[bool] = typer.Option(
        None,
        "--notify-on-start/--no-notify-on-start",
        help="Enable or disable notification on start.",
    ),
    cluster_id: Optional[int] = typer.Option(
        None,
        "--cluster-id",
        "--clusterid",
        help="Id (Cluster).",
    ),
    file_transfer_method_id: Optional[int] = typer.Option(
        None,
        "--file-transfer-method-id",
        help="File transfer method identifier.",
    ),
    reservation: Optional[str] = typer.Option(
        None, "--reservation", help="Reservation name."
    ),
    is_extra_long: Optional[bool] = typer.Option(
        None,
        "--is-extra-long/--not-extra-long",
        help="Mark the job as extra-long.",
    ),
    job_environment_variable: Annotated[
        Optional[List[str]],
        typer.Option(
            "--job-environment-variable",
            help="Override a job environment variable as envIndex:field:value.",
        ),
    ] = None,
    task_name: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-name",
            help="Override a task name as taskIndex:value.",
        ),
    ] = None,
    task_min_cores: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-min-cores",
            help="Override task minimum cores as taskIndex:value.",
        ),
    ] = None,
    task_max_cores: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-max-cores",
            help="Override task maximum cores as taskIndex:value.",
        ),
    ] = None,
    task_gpu_cores: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-gpu-cores",
            help="Override task GPU cores as taskIndex:value.",
        ),
    ] = None,
    task_gpu_nodes: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-gpu-nodes",
            help="Override task GPU nodes as taskIndex:value.",
        ),
    ] = None,
    walltime_limit: Annotated[
        Optional[List[str]],
        typer.Option(
            "--walltime-limit",
            "--walltimelimit",
            help="Override task walltime as taskIndex:value.",
        ),
    ] = None,
    task_placement_policy: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-placement-policy",
            help="Override task placement policy as taskIndex:value.",
        ),
    ] = None,
    task_priority: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-priority",
            help="Override task priority as taskIndex:value.",
        ),
    ] = None,
    task_job_arrays: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-job-arrays",
            help="Override task job arrays as taskIndex:value.",
        ),
    ] = None,
    task_is_exclusive: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-is-exclusive",
            help="Override task exclusivity as taskIndex:true|false.",
        ),
    ] = None,
    task_is_rerunnable: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-is-rerunnable",
            help="Override task rerunnable flag as taskIndex:true|false.",
        ),
    ] = None,
    task_standard_input_file: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-standard-input-file",
            help="Override task standard input file as taskIndex:value.",
        ),
    ] = None,
    task_standard_output_file: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-standard-output-file",
            help="Override task standard output file as taskIndex:value.",
        ),
    ] = None,
    task_standard_error_file: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-standard-error-file",
            help="Override task standard error file as taskIndex:value.",
        ),
    ] = None,
    task_progress_file: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-progress-file",
            help="Override task progress file as taskIndex:value.",
        ),
    ] = None,
    task_log_file: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-log-file",
            help="Override task log file as taskIndex:value.",
        ),
    ] = None,
    task_cluster_task_subdirectory: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-cluster-task-subdirectory",
            help="Override task cluster subdirectory as taskIndex:value.",
        ),
    ] = None,
    cluster_node_type_id: Annotated[
        Optional[List[str]],
        typer.Option(
            "--cluster-node-type-id",
            "--clusternodetypeid",
            help="Override task cluster node type as taskIndex:value.",
        ),
    ] = None,
    cmd_template_id: Annotated[
        Optional[List[str]],
        typer.Option(
            "--cmd-template-id",
            "--cmdtemplateid",
            help="Override task command template id as taskIndex:value.",
        ),
    ] = None,
    task_cpu_hyper_threading: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-cpu-hyper-threading",
            help="Override task CPU hyper-threading as taskIndex:true|false.",
        ),
    ] = None,
    task_required_node: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-required-node",
            help="Override required nodes as taskIndex:itemIndex:value.",
        ),
    ] = None,
    task_parallelization_parameter: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-parallelization-parameter",
            help="Override parallelization parameters as taskIndex:itemIndex:field:value.",
        ),
    ] = None,
    task_environment_variable: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-environment-variable",
            help="Override task environment variables as taskIndex:itemIndex:field:value.",
        ),
    ] = None,
    task_memory: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-memory",
            help="Override task memory as taskIndex:value.",
        ),
    ] = None,
    task_memory_per_cpu: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-memory-per-cpu",
            help="Override task memory per CPU as taskIndex:value.",
        ),
    ] = None,
    task_memory_per_gpu: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-memory-per-gpu",
            help="Override task memory per GPU as taskIndex:value.",
        ),
    ] = None,
    task_depends_on: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-depends-on",
            help="Override task dependencies as taskIndex:itemIndex:field:value.",
        ),
    ] = None,
    cmdTemplateParameters: Annotated[
        Optional[List[str]],
        typer.Option(
            "--cmd-template-parameters",
            help="Command template parameters for task 0 in key:value format.",
        ),
    ] = None,
    task_template_parameter_value: Annotated[
        Optional[List[str]],
        typer.Option(
            "--task-template-parameter-value",
            help="Override task template parameter values as taskIndex:itemIndex:field:value.",
        ),
    ] = None,
    save_result_job_specification: bool = typer.Option(
        False,
        "--save-result-job-specification",
        help=(
            "Save the resulting job specification JSON to the current working "
            f"directory as {DEFAULT_RESULT_JOB_SPECIFICATION_FILENAME}."
        ),
    ),
):
    """Create HPC job"""
    try:
        utils.print_and_log("Creating new HPC job ...")

        parsed_job_specification = parse_job_specification(
            json_job_spec_file=json_job_spec_file,
            job_overrides={
                "SessionCode": session_code,
                "Name": name,
                "ProjectId": project_id,
                "SubProjectIdentifier": sub_project_identifier,
                "WaitingLimit": waiting_limit,
                "NotificationEmail": notification_email,
                "PhoneNumber": phone_number,
                "NotifyOnAbort": notify_on_abort,
                "NotifyOnFinish": notify_on_finish,
                "NotifyOnStart": notify_on_start,
                "ClusterId": cluster_id,
                "FileTransferMethodId": file_transfer_method_id,
                "Reservation": reservation,
                "IsExtraLong": is_extra_long,
            },
            task_scalar_overrides={
                "Name": (task_name, str, "--task-name"),
                "MinCores": (task_min_cores, int, "--task-min-cores"),
                "MaxCores": (task_max_cores, int, "--task-max-cores"),
                "GpuCores": (task_gpu_cores, int, "--task-gpu-cores"),
                "GpuNodes": (task_gpu_nodes, int, "--task-gpu-nodes"),
                "WalltimeLimit": (walltime_limit, int, "--walltime-limit"),
                "PlacementPolicy": (
                    task_placement_policy,
                    str,
                    "--task-placement-policy",
                ),
                "Priority": (
                    task_priority,
                    lambda raw_value: _normalize_task_priority_value(
                        raw_value, "--task-priority"
                    ),
                    "--task-priority",
                ),
                "JobArrays": (task_job_arrays, str, "--task-job-arrays"),
                "IsExclusive": (task_is_exclusive, bool, "--task-is-exclusive"),
                "IsRerunnable": (
                    task_is_rerunnable,
                    bool,
                    "--task-is-rerunnable",
                ),
                "StandardInputFile": (
                    task_standard_input_file,
                    str,
                    "--task-standard-input-file",
                ),
                "StandardOutputFile": (
                    task_standard_output_file,
                    str,
                    "--task-standard-output-file",
                ),
                "StandardErrorFile": (
                    task_standard_error_file,
                    str,
                    "--task-standard-error-file",
                ),
                "ProgressFile": (task_progress_file, str, "--task-progress-file"),
                "LogFile": (task_log_file, str, "--task-log-file"),
                "ClusterTaskSubdirectory": (
                    task_cluster_task_subdirectory,
                    str,
                    "--task-cluster-task-subdirectory",
                ),
                "ClusterNodeTypeId": (
                    cluster_node_type_id,
                    int,
                    "--cluster-node-type-id",
                ),
                "CommandTemplateId": (
                    cmd_template_id,
                    int,
                    "--cmd-template-id",
                ),
                "CpuHyperThreading": (
                    task_cpu_hyper_threading,
                    bool,
                    "--task-cpu-hyper-threading",
                ),
                "Memory": (task_memory, int, "--task-memory"),
                "MemoryPerCPU": (
                    task_memory_per_cpu,
                    int,
                    "--task-memory-per-cpu",
                ),
                "MemoryPerGPU": (
                    task_memory_per_gpu,
                    int,
                    "--task-memory-per-gpu",
                ),
            },
            job_environment_variables=job_environment_variable,
            task_required_nodes=task_required_node,
            task_depends_on=task_depends_on,
            task_parallelization_parameters=task_parallelization_parameter,
            task_environment_variables=task_environment_variable,
            task_template_parameter_values=task_template_parameter_value,
            cmd_template_parameters=cmdTemplateParameters,
        )

        if save_result_job_specification:
            result_file_path = Path.cwd() / DEFAULT_RESULT_JOB_SPECIFICATION_FILENAME
            result_file_path.write_text(
                json.dumps(parsed_job_specification.to_dict(), indent=4),
                encoding="utf-8",
            )
            utils.print_and_log(
                "Resulting job specification was saved in: "
                f"{result_file_path.resolve()}"
            )

        body = {
            "_preload_content": False,
            "body": parsed_job_specification,
        }

        response = heappeCore.JobManagementApi(
            configuration.get_api_instance()
        ).heappe_job_management_create_job_post(**body)
        jobId = json.loads(response.data)["Id"]
        utils.print_and_log(f"\nHPC job was created (Id: {jobId})")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(
                response_data["title"], response_data["detail"], response_data["status"]
            ) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException(
                "Link to a HEAppE instance is not set or valid. Please check Conf Init option."
            ) from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except Exception as exception:
        raise exceptions.Py4HEAppEInternalException(
            f"Other exception: {str(exception)}"
        ) from None


@app.command(name="Submit")
def submit_job(id: int = typer.Option(..., help="Id (HPC job)")):
    """Submit HPC job"""
    try:
        utils.print_and_log("Submitting HPC job ...")
        body = {
            "_preload_content": False,
            "body": {
                "CreatedJobInfoId": id,
                "SessionCode": utils.load_stored_session(),
            },
        }

        _ = heappeCore.JobManagementApi(
            configuration.get_api_instance()
        ).heappe_job_management_submit_job_put(**body)
        utils.print_and_log(f"\nHPC job was submitted successfully.")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(
                response_data["title"], response_data["detail"], response_data["status"]
            ) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException(
                "Link to a HEAppE instance is not set or valid. Please check Conf Init option."
            ) from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except Exception as exception:
        raise exceptions.Py4HEAppEInternalException(
            f"Other exception: {str(exception)}"
        ) from None


@app.command(name="Cancel")
def cancel_job(id: int = typer.Option(..., help="Id (HPC job)")):
    """Cancel HPC job"""
    try:
        utils.print_and_log("Cancelling HPC job ...")
        body = {
            "_preload_content": False,
            "body": {
                "SubmittedJobInfoId": id,
                "SessionCode": utils.load_stored_session(),
            },
        }

        _ = heappeCore.JobManagementApi(
            configuration.get_api_instance()
        ).heappe_job_management_cancel_job_put(**body)
        utils.print_and_log(f"\nHPC job was cancelled.")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(
                response_data["title"], response_data["detail"], response_data["status"]
            ) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException(
                "Link to a HEAppE instance is not set or valid. Please check Conf Init option."
            ) from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except Exception as exception:
        raise exceptions.Py4HEAppEInternalException(
            f"Other exception: {str(exception)}"
        ) from None


@app.command(name="Delete")
def delete_job(
    id: int = typer.Option(..., help="Id (HPC job)"),
    archiveLogs: bool = typer.Option(True, help="Archive job logs; default is true"),
):
    """Delete HPC job"""
    try:
        utils.print_and_log("Deleting HPC job ...")
        body = {
            "_preload_content": False,
            "body": {
                "SubmittedJobInfoId": id,
                "SessionCode": utils.load_stored_session(),
                "ArchiveLogs": archiveLogs,
            },
        }

        _ = heappeCore.JobManagementApi(
            configuration.get_api_instance()
        ).heappe_job_management_delete_job_delete(**body)
        utils.print_and_log("\nHPC job was deleted successfully.")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(
                response_data["title"], response_data["detail"], response_data["status"]
            ) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException(
                "Link to a HEAppE instance is not set or valid. Please check Conf Init option."
            ) from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except Exception as exception:
        raise exceptions.Py4HEAppEInternalException(
            f"Other exception: {str(exception)}"
        ) from None


@app.command(name="List")
def list_jobs(
    jobStates: Annotated[
        Optional[List[str]],
        typer.Option(
            help="HPC job states to filter by; value can be 1, 2, 4, 8, 16 or 32; repeat the option to filter by multiple job states."
        ),
    ] = None,
):
    """List HPC jobs"""
    try:
        utils.print_and_log("Listing HPC job(s) ...")
        parameters = {
            "_preload_content": False,
            "SessionCode": utils.load_stored_session(),
        }

        if jobStates:
            parameters["JobStates"] = ",".join(jobStates)

        response = heappeCore.JobManagementApi(
            configuration.get_api_instance()
        ).heappe_job_management_list_jobs_for_current_user_get(**parameters)
        print(f"\nHPC jobs:\n{json.dumps(json.loads(response.data), indent = 3)}")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(
                response_data["title"], response_data["detail"], response_data["status"]
            ) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException(
                "Link to a HEAppE instance is not set or valid. Please check Conf Init option."
            ) from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except Exception as exception:
        raise exceptions.Py4HEAppEInternalException(
            f"Other exception: {str(exception)}"
        ) from None


@app.command(name="Info")
def get_job_info(id: int = typer.Option(..., help="Id (HPC job)")):
    """Get Current HPC job info"""
    try:
        utils.print_and_log("Getting current HPC job info ...")
        parameters = {
            "_preload_content": False,
            "SubmittedJobInfoId": id,
            "SessionCode": utils.load_stored_session(),
        }

        response = heappeCore.JobManagementApi(
            configuration.get_api_instance()
        ).heappe_job_management_current_info_for_job_get(**parameters)
        print(f"\nHPC job info:\n{json.dumps(json.loads(response.data), indent = 3)}")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(
                response_data["title"], response_data["detail"], response_data["status"]
            ) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException(
                "Link to a HEAppE instance is not set or valid. Please check Conf Init option."
            ) from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except Exception as exception:
        raise exceptions.Py4HEAppEInternalException(
            f"Other exception: {str(exception)}"
        ) from None


@app.command(name="CopyDataToTemp")
def copy_data_to_temp(
    id: int = typer.Option(..., help="Id (HPC job)"),
    path: str = typer.Option(..., help="Path containing data to be copied"),
):
    """Copy data to temp location"""
    try:
        utils.print_and_log("Copying HPC job data to temporary location ...")
        session_code = utils.load_stored_session()
        body = {
            "_preload_content": False,
            "body": {"CreatedJobInfoId": id, "Path": path, "SessionCode": session_code},
        }

        heappeCore.JobManagementApi(
            configuration.get_api_instance()
        ).heappe_job_management_copy_job_data_to_temp_post(**body)
        utils.print_and_log(
            f"\nSpecific data was successfully copied to temporary location."
        )
        print(f"Temp SessionCode for copying the data is: {session_code}.")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(
                response_data["title"], response_data["detail"], response_data["status"]
            ) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException(
                "Link to a HEAppE instance is not set or valid. Please check Conf Init option."
            ) from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except Exception as exception:
        raise exceptions.Py4HEAppEInternalException(
            f"Other exception: {str(exception)}"
        ) from None


@app.command(name="CopyDataFromTemp")
def copy_data_from_temp(
    id: int = typer.Option(..., help="Id (HPC job)"),
    temporaryHash: str = typer.Option(..., help="Path containing data to be copied"),
):
    """Copy data from temp location"""
    try:
        utils.print_and_log(
            "Copying HPC job data from temporary location to job directory..."
        )
        body = {
            "_preload_content": False,
            "body": {
                "CreatedJobInfoId": id,
                "TempSessionCode": temporaryHash,
                "SessionCode": utils.load_stored_session(),
            },
        }

        response = heappeCore.JobManagementApi(
            configuration.get_api_instance()
        ).heappe_job_management_copy_job_data_from_temp_post(**body)
        # NOTE: response is not deserialized into a python object
        utils.print_and_log(f"\n{response.data}")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(
                response_data["title"], response_data["detail"], response_data["status"]
            ) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException(
                "Link to a HEAppE instance is not set or valid. Please check Conf Init option."
            ) from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except Exception as exception:
        raise exceptions.Py4HEAppEInternalException(
            f"Other exception: {str(exception)}"
        ) from None


@app.command(name="GetAllocatedNodes")
def get_allocated_nodes_ip(taskId: int = typer.Option(..., help="Id (HPC task)")):
    """Get HPC Task allocated nodes addresses (IP)"""
    try:
        utils.print_and_log("Getting HPC task allocated nodes addresses (IP) ...")
        parameters = {
            "_preload_content": False,
            "SubmittedTaskInfoId": taskId,
            "SessionCode": utils.load_stored_session(),
        }

        response = heappeCore.JobManagementApi(
            configuration.get_api_instance()
        ).heappe_job_management_allocated_nodes_ips_get(**parameters)
        # NOTE: response is not deserialized into a python object
        utils.print_and_log(
            f"\nHPC task {taskId} uses the following nodes: {response.data}"
        )

    except rest.ApiException as exception:
        try:
            if exception.body:
                response_data = json.loads(exception.body)
                raise exceptions.Py4HEAppEAPIException(
                    response_data["title"],
                    response_data["detail"],
                    response_data["status"],
                ) from None
            raise exceptions.Py4HEAppEAPIException(
                "Unknown Error", exception.reason, exception.status
            ) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException(
                "Link to a HEAppE instance is not set or valid. Please check Conf Init option."
            ) from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
        raise exceptions.Py4HEAppEException(exception.message) from None

    except Exception as exception:
        raise exceptions.Py4HEAppEInternalException(
            f"Other exception: {str(exception)}"
        ) from None


if __name__ == "__main__":
    app()
