<img align="right" width="35%" src="docs/imgs/logo.png?sanitize=true">

# Py4HEAppE (Python for HEAppE Middleware)

Py4HEAppE simplifies access to the [HEAppE](https://heappe.eu) features by providing a high-level Python interface that abstracts away the complexities of direct API interactions. This allows users to focus on their core tasks without worrying about the underlying details of API communication. It can be usable in <b>two modes</b> depends what the end-user needs:
- HEAppE CLI Commands
- HEAppE API Wrapper Library

## Key Benefits

### Ease of Use:
Py4HEAppE provides a straightforward and intuitive interface for interacting with the HEAppE API. Users can perform complex operations with simple function calls.

### Abstraction: 
The library abstracts the intricacies of the HEAppE API, allowing users to work with high-level concepts and operations.

### Efficiency: 
By using Py4HEAppE, users can quickly integrate HEAppE functionalities into their Python applications, reducing development time and effort.

### Consistency:
The library ensures consistent and reliable communication with the HEAppE API, handling errors and edge cases gracefully.

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python (version 3.11)
* Access to Deployed HEAppE instance (HEAppE instance URL and HPC project identificator)

### Installation

1. Clone the repo
   ```sh
   git clone -b develop https://code.it4i.cz/ADAS-Private/HEAppE/clientapplications/Py4HEAppE.git
   ```
2. Go to cloned dir
   ```sh
   cd Py4HEAppE
   ```
3. Install Py4HEAppE and dependencies
    ```
    pip install .
    ```


<b>Note:</b> In some cases, you can obtain a warning message like this <b>"WARNING: The script py4heappe.exe is installed in 'C:\Users\user\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.</b>" If you obtained a similar warning message, it is necessary to add the mentioned path into your operation system <b>PATH</b> variable or use a path with an executable file (i.e. C:\Users\user\AppData\Roaming\Python\Python311\Scripts\py4heappe.exe).

## HEAppE CLI

The HEAppE CLI (Command Line Interface) provides a convenient way to interact with the HEAppE Middleware directly from your terminal. It allows users to perform various operations such as authentication, job management, and information retrieval without needing to write any code. This makes it an ideal tool for end-users who need to manage HEAppE Instance efficiently.

### Usage
For using HEAppE CLI it is neeaded to initializing Py4HEAppE for usage with a specific HEAppE Instance (It is necessary to call for the first usage). Command requires <b>HPC project accounting string</b> and <b>HEAppE Instance URL</b>.

```shell
# Initial Setup
py4heappe Config Init
```

All mentioned functions are aggregated to the specific groups available from CLI. To do so, type the following to provide help on how to use managers via CLI.

```shell
# List of available groups
py4heappe --help 
```

Available groups: 

```shell
# Authentication Group
py4heappe Auth --help 

# Command Template Management Group
py4heappe CmdTemplateMgmt --help 

# Information Group
py4heappe Info --help 

# Report Group
py4heappe Report --help 
```

<b>Note:</b> On Windows operation system need to use <b>"py4heappe.exe"</b> instead of <b>"py4heappe"</b>.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## HEAppE API Wrapper Library

In this mode, the Py4HEAppE package is used as a wrapper for HEAppE API specification. It allows users to perform various operations from <b>HEAppE API</b>, such as authentication, job management, and information retrieval, without needing to write their API wrapper code. It can be easily integrated with internal <b>Python</b> projects that HEAppE Middleware wants to be used. More information about usability can be found in the section below.
 
### Usage
 
It is required to specify following modules in "requirements.txt" file.
 
```text
paramiko==3.5.0
scp==0.15.0
urllib3==2.2.3
py4heappe @ git+https://github.com/It4innovations/Py4HEAppE.git
```

The code snapshot illustrated an example of "how to" obtain cluster information from the HEAppE Instance. For more detailed examples of basic HPC workflow, please refer to the [example.py](docs/examples/example.py) file.

```python
import json
import os
import time
from io import StringIO
from pathlib import Path
 
import py4heappe.core as hp
 
print("\nFetching cluster info...")
lac_body = {
    "_preload_content": False
}
 
ciEndpoint = hp.ClusterInformationApi(api_instance)
r = ciEndpoint.heappe_cluster_information_list_available_clusters_get(**lac_body)
r_data = json.loads(r.data)
print(json.dumps(r_data, indent = 3))
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](LICENSE.txt) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Requirements

This section contains dependencies and tools that are required for Py4HEAppE.

### Packages

- [Paramiko (3.5.0)](https://pypi.org/project/paramiko/3.5.0/)
- [Scp (0.15.0)](https://pypi.org/project/scp/0.15.0/)
- [Urllib3 (2.2.3)](https://pypi.org/project/urllib3/2.2.3/)
- [Certifi (2024.8.30)](https://pypi.org/project/certifi/2024.8.30/)
- [Six (1.16.0)](https://pypi.org/project/six/1.16.0/)
- [Typer (0.13.1)](https://pypi.org/project/typer/0.9.0/)
- [Python-dotenv (1.0.1)](https://pypi.org/project/python-dotenv/1.0.1/)
- [Validators (0.34.0)](https://pypi.org/project/validators/0.34.0/)
- [Py4Lexis (2.2.3)](https://opencode.it4i.eu/lexis-platform/clients/py4lexis)

### Tools

The API Wrapper was partly generated by [online tool](https://editor.swagger.io).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgement

e-Infra CZ
This work was supported by the Ministry of Education, Youth and Sports of the Czech Republic through the e-INFRA CZ (ID:90254)

<p align="right">(<a href="#readme-top">back to top</a>)</p>