<img align="right" width="35%" src="https://raw.githubusercontent.com/It4innovations/Py4HEAppE/refs/heads/master/docs/imgs/logo.png">

# Py4HEAppE (Python for HEAppE Middleware)
Py4HEAppE provides both a command-line interface and versioned Python wrappers for the [HEAppE](https://heappe.eu) middleware API.

You can use it in two ways:
- HEAppE CLI commands for interactive and scripting use
- Versioned Python API wrappers for direct integration into your own applications

## Supported HEAppE Versions
| Py4HEAppE | HEAppE Version | Notes |
| :-------: | :------------- | :---- |
| 2.9.X | 6.4.X, 6.3.X, 6.2.X, 6.2.1, 5.0.X, 4.3.X, 4.2.X | Without Admin CLI section |
| 2.8.X | 6.4.X, 6.3.X, 6.2.X, 6.2.1, 5.0.X, 4.3.X, 4.2.X | Without Admin CLI section |
| 2.7.X | 6.4.X, 6.3.X, 6.2.X, 6.2.1, 5.0.X, 4.3.X, 4.2.X | Without Admin CLI section |
| 2.6.X | 6.3.X, 6.2.X, 6.1.X, 5.0.X, 4.3.X, 4.2.X | Without Admin CLI section |
| 2.5.X | 6.3.X, 6.2.X, 6.1.X, 5.0.X, 4.3.X, 4.2.X | Without Admin CLI section |
| 2.4.X | 6.1.X, 6.0.X, 5.0.X, 4.3.X, 4.2.X | Without Admin CLI section |
| 2.3.X | 6.0.X, 5.0.X, 4.3.X, 4.2.X | Without Admin CLI section |
| 2.2.X | 5.0.X, 4.3.X, 4.2.X | Without Admin CLI section |
| 2.1.X | 5.0.X, 4.3.X, 4.2.X | Without Admin, Job, and File CLI sections |
| 2.0.X | 5.0.X | Without Admin, Job, and File CLI sections |
| 1.X.X | 4.3.X, 4.2.X | Without Admin, Job, and File CLI sections |

## Requirements
- Python 3.11 or newer
- Access to a deployed HEAppE instance
- HEAppE instance URL
- HEAppE accounting string for the target computational project

## Installation
If the `py4heappe` executable is not on your `PATH`, use the full path to the installed script or add the script directory to `PATH`.

On Windows, use `py4heappe.exe` instead of `py4heappe`.

## HEAppE CLI
The CLI is intended for users who want to work with HEAppE directly from a terminal without writing Python code.

### Initial Setup
Before using the CLI for the first time, initialize the HEAppE instance URL and the accounting string:

```shell
py4heappe Conf Init
```

### Available Command Groups
```shell
py4heappe --help
```

Current command groups:

- `Conf` for local CLI configuration
- `Auth` for authentication
- `CmdTemp` for command template operations
- `Info` for version and cluster information
- `Job` for job lifecycle management
- `FileTransfer` for job file upload and download operations
- `Report` for resource usage and reporting

### Useful Help Commands

```shell
py4heappe Auth --help
py4heappe Info --help
py4heappe Job --help
py4heappe FileTransfer --help
py4heappe Report --help
```

### Basic CLI Examples

Authenticate with username and password:

```shell
py4heappe Auth UserPass
```

Show the HEAppE API version:

```shell
py4heappe Info Version
```

List available clusters:

```shell
py4heappe Info ClusterInfo
```

List your jobs:

```shell
py4heappe Job List
```

### Create a Job from a JSON Template

Py4HEAppE supports a JSON-first workflow for job creation.

Generate a minimal job specification template in the current directory:

```shell
py4heappe Job InitJobSpecification
```

Generate the full swagger-shaped job specification template instead:

```shell
py4heappe Job InitJobSpecification --full
```

Or generate it in a specific directory or target file:

```shell
py4heappe Job InitJobSpecification --file-destination ./job_specs
py4heappe Job InitJobSpecification --file-destination ./job_specs/demo_job.json
```

Create a job from the JSON file and override selected values from the command line:

```shell
py4heappe Job Create --json-job-spec-file ./job_specification.json \
    --name demo-job \
    --cluster-id 2 \
    --project-id 1 \
    --task-name 0:demo-task \
    --task-max-cores 0:128 \
    --walltime-limit 0:1800 \
    --cluster-node-type-id 0:18 \
    --cmd-template-id 0:3 \
    --cmd-template-parameters inputParam:testValue
```

CLI overrides always take precedence over values loaded from `--json-job-spec-file`.

Save the final parsed job specification that will be submitted to HEAppE:

```shell
py4heappe Job Create --json-job-spec-file ./job_specification.json \
    --save-result-job-specification
```

This writes `resultJobSpecJson.json` into the current working directory.

### Override Format for Nested Task Data

Some `Job Create` options work on indexed task items and nested collections.

Examples:

```shell
# Task scalar override
py4heappe Job Create --json-job-spec-file ./job_specification.json --task-name 0:main-task

# Task environment variable override
py4heappe Job Create --json-job-spec-file ./job_specification.json \
  --task-environment-variable 0:0:Name:OMP_NUM_THREADS \
  --task-environment-variable 0:0:Value:8

# Task template parameter override
py4heappe Job Create --json-job-spec-file ./job_specification.json \
  --task-template-parameter-value 0:0:CommandParameterIdentifier:inputParam \
  --task-template-parameter-value 0:0:ParameterValue:testValue
```

### File Transfer Examples

List files changed during job execution:

```shell
py4heappe FileTransfer ListChanged --help
```

Download a single file from a job directory:

```shell
py4heappe FileTransfer Download --help
```

Upload files directly into the job execution directory:

```shell
py4heappe FileTransfer Stream --help
```

## Python API Wrapper

Py4HEAppE also ships versioned Python wrappers generated from the HEAppE API.

Use the wrapper that matches your target HEAppE version:

```python
import py4heappe.heappe_v6.core as hp
# or:
# import py4heappe.heappe_v5.core as hp
# import py4heappe.heappe_v4.core as hp
```

There is no single unversioned `py4heappe.core` module. Use the versioned wrapper explicitly.

### Minimal Python Example

```python
import json

import py4heappe.heappe_v6.core as hp

configuration = hp.Configuration()
configuration.host = "https://heappe.example.org"
api_client = hp.ApiClient(configuration)

try:
    auth_api = hp.UserAndLimitationManagementApi(api_client)
    management_api = hp.ManagementApi(api_client)
    cluster_api = hp.ClusterInformationApi(api_client)

    auth_body = {
        "_preload_content": False,
        "body": {
            "Credentials": {
                "Username": "username",
                "Password": "password",
            }
        },
    }

    auth_response = auth_api.heappe_user_and_limitation_management_authenticate_user_password_post(
        **auth_body
    )
    session_code = json.loads(auth_response.data)

    version_response = management_api.heappe_management_version_information_get(
        _preload_content=False,
        SessionCode=session_code,
    )
    print(json.dumps(json.loads(version_response.data), indent=2))

    cluster_response = cluster_api.heappe_cluster_information_list_available_clusters_get(
        _preload_content=False,
        SessionCode=session_code,
    )
    print(json.dumps(json.loads(cluster_response.data), indent=2))

finally:
    api_client.pool.close()
    api_client.pool.join()
```

### Create a Job Through the Python Wrapper

```python
import json

import py4heappe.heappe_v6.core as hp

configuration = hp.Configuration()
configuration.host = "https://heappe.example.org"
api_client = hp.ApiClient(configuration)

try:
    job_api = hp.JobManagementApi(api_client)

    body = {
        "_preload_content": False,
        "body": {
            "SessionCode": "your-session-code",
            "JobSpecification": {
                "Name": "demo-job",
                "ProjectId": 1,
                "ClusterId": 2,
                "FileTransferMethodId": 1,
                "Tasks": [
                    {
                        "Name": "demo-task",
                        "MinCores": 1,
                        "MaxCores": 16,
                        "WalltimeLimit": 1800,
                        "StandardOutputFile": "stdout",
                        "StandardErrorFile": "stderr",
                        "ProgressFile": "stdprog",
                        "LogFile": "stdlog",
                        "ClusterNodeTypeId": 18,
                        "CommandTemplateId": 3,
                        "TemplateParameterValues": [
                            {
                                "CommandParameterIdentifier": "inputParam",
                                "ParameterValue": "testValue",
                            }
                        ],
                    }
                ],
            },
        },
    }

    response = job_api.heappe_job_management_create_job_post(**body)
    job_id = json.loads(response.data)["Id"]
    print(f"Created job: {job_id}")

finally:
    api_client.pool.close()
    api_client.pool.join()
```

## Notes

- CLI configuration is stored locally after `py4heappe Conf Init`.
- Most CLI commands require a valid session, so authenticate before running job or file-transfer operations.
- For detailed option lists, use the built-in `--help` on each command group and subcommand.

## Acknowledgement

This work was supported by the Ministry of Education, Youth and Sports of the Czech Republic through e-INFRA CZ (ID:90254).
