import dotenv
import os
import typer
import validators

import py4heappe.core as hp
import py4heappe.core.base.utils as utils
from py4heappe.core.base import exceptions


app = typer.Typer(name="HEAppEConfigurationCLI", no_args_is_help=True, pretty_exceptions_show_locals=False)

def get_api_instance():
    dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    url : str = os.environ.get("url")

    if url is None:
        raise exceptions.Py4HEAppEInternalException("The Py4HEAppE is not configured. Must be configured first.") from None
    
    configuration = hp.Configuration()
    configuration.host = url
    api_instance = hp.ApiClient(configuration)
    return api_instance

def get_project_from_configuration():
    dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

    computationalProject : str = os.environ.get("project")
    if computationalProject is None:
        raise exceptions.Py4HEAppEInternalException("The Py4HEAppE is not configured. Must be configured first.") from None

    return computationalProject

@app.command(name="Init")
def environment_preparation():
    """Preparation of Py4HEAppE Environment"""
    utils.print_and_log("Preparation of Py4HEAppE Environment")
    dotenv.load_dotenv()

    url: str = os.environ.get("url")
    computationalProject: str = os.environ.get("project")

    if url is not None or computationalProject is not None:
        reconfigure = typer.confirm(f"Py4HEAppE is already configured (URL: \"{url}\", HPC Computational project \"{computationalProject}\").\nDo you want to reconfigure it?")
        if not reconfigure:
            return

    url = typer.prompt("Enter the HEAppE address (for example: https://heappe.it4i.cz/presentation)")
    if not validators.url(url):
        raise exceptions.Py4HEAppEInternalException("The provided HEAppE URL is not valid.") from None
    
    if "/swagger/index.html" in url:
        url = url.replace("/swagger/index.html", "")

    computationalProject = typer.prompt("Enter HPC Computational project", confirmation_prompt=True)

    dotenv.set_key(os.path.join(os.path.dirname(__file__), '.env'), "url", url)
    dotenv.set_key(os.path.join(os.path.dirname(__file__), '.env'), "project", computationalProject)

    utils.print_and_log("Py4HEAppE is configured.")
    return


if __name__ == '__main__':
    app()