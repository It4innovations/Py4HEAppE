import json
import typer

import py4heappe.cli.configuration as configuration
import py4heappe.cli.information as infoCLI
import py4heappe.core.base.utils as utils
import py4heappe.core as heappeCore

from py4heappe.core.base import exceptions
from py4heappe.core  import rest 


app = typer.Typer(name="HEAppECommandTemplateCLI", no_args_is_help=True, pretty_exceptions_short=True)

@app.command(name="List")
def get_command_templates_for_project():
    """List Command Templates for configured HPC Project"""
    try:      
        utils.print_and_log("Listing Command Templates for configured HPC Project ...") 
        projectId : int = infoCLI.get_hpc_project()["Id"]
        parameters = {
            "_preload_content": False,
            "ProjectId": projectId,
            "SessionCode": utils.load_stored_session()
        }

        response = heappeCore.ManagementApi(configuration.get_api_instance()).heappe_management_command_templates_get(**parameters)
        commandTemplates =  json.loads(response.data)
        print(f"\nCommand Templates for HPC project {projectId}:")
        print(json.dumps(commandTemplates, indent = 3))
        
    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(response_data['title'], response_data['detail'], response_data['status']) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException("HEAppE is not listening on specific address") from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None 
    
    except Exception:
        raise exceptions.Py4HEAppEException(f"Other exception: {exception.message}") from None

@app.command("Create")
def create_command_template(Name:str = typer.Option(..., help='Command Template Name'),
                           desc:str = typer.Option(..., help='Command Template Description'),
                           extAllocCommand:str = typer.Option(None, help='Command Template Extended Allocation Command'),
                           execScript:str = typer.Option(..., help='Path to executable file/script for Command Template'),
                           prepScript:str = typer.Option(None, help='Path to preparation executable script for Command Template or Specific Bash Commands (ml mpi;cp ...)'),
                           clusterNodeTypeId:int = typer.Option(..., help='Cluster Node Type Identifier')):
    """Create Command Template for configured HPC Project"""
    try:
        utils.print_and_log("Creating Command Template for configured HPC Project ...")
        body = {
            "_preload_content": False,
            "body": {
                "Name": Name,
                "Description": desc,
                "ExtendedAllocationCommand": extAllocCommand,
                "PreparationScript": prepScript,
                "ExecutableFile": execScript,
                "ClusterNodeTypeId": clusterNodeTypeId,
                "TemplateParameters": [],
                "ProjectId": infoCLI.get_hpc_project()["Id"],
                "SessionCode": utils.load_stored_session()
            }
        }

        response = heappeCore.ManagementApi(configuration.get_api_instance()).heappe_management_command_template_post(**body)
        commandTemplateId =  json.loads(response.data)["Id"]
        utils.print_and_log(f"\nCommand Template was created (Id: {commandTemplateId})")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(response_data['title'], response_data['detail'], response_data['status']) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException("HEAppE is not listening on specific address") from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None 
    
    except Exception:
        raise exceptions.Py4HEAppEException(f"Other exception: {exception.message}") from None

@app.command("Modify")
def modify_command_template(id:int = typer.Option(..., help='Command Template Identifier'),
                            Name:str = typer.Option(..., help='Command Template Name'),
                            desc:str = typer.Option(..., help='Command Template Description'),
                            extAllocCommand:str = typer.Option(None, help='Command Template Extended Allocation Command'),
                            execScript:str = typer.Option(..., help='Path to executable file/script for Command Template'),
                            prepScript:str = typer.Option(None, help='Path to preparation executable script for Command Template or Specific Bash Commands (ml mpi;cp ...)'),
                            clusterNodeTypeId:int = typer.Option(None, help='Cluster Node Type Identifier')):
    """Modify Command Template for configured HPC Project"""
    try:
        utils.print_and_log("Modification Command Template for configured HPC Project ...")
        body = {
            "_preload_content": False,
            "body": {
                "Id": id,
                "Name": Name,
                "Description": desc,
                "ExtendedAllocationCommand": extAllocCommand,
                "PreparationScript": prepScript,
                "ExecutableFile": execScript,
                "ClusterNodeTypeId": clusterNodeTypeId,
                "TemplateParameters": [],
                "SessionCode": utils.load_stored_session()
            }
        }

        _ = heappeCore.ManagementApi(configuration.get_api_instance()).heappe_management_command_template_put(**body)
        utils.print_and_log(f"\nCommand Template was modified.")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(response_data['title'], response_data['detail'], response_data['status']) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException("HEAppE is not listening on specific address") from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None 
    
    except Exception:
        raise exceptions.Py4HEAppEException(f"Other exception: {exception.message}") from None

@app.command("Remove")
def remove_command_template(id:int = typer.Option(..., help='Command Template Identifier')):
    """Remove Command Template for configured HPC Project"""
    try:
        utils.print_and_log("Removing Command Template for configured HPC Project ...")
        body = {
            "_preload_content": False,
            "body": {
                "CommandTemplateId": id,
                "SessionCode": utils.load_stored_session()
            }
        }
        
        _ = heappeCore.ManagementApi(configuration.get_api_instance()).heappe_management_remove_command_template_delete(**body)
        utils.print_and_log("\nCommand Template was removed.")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(response_data['title'], response_data['detail'], response_data['status']) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException("HEAppE is not listening on specific address") from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None 
    
    except Exception:
        raise exceptions.Py4HEAppEException(f"Other exception: {exception.message}") from None

@app.command("CreateFromGeneric")
def create_command_template_from_generic(id:str = typer.Option(..., help='Generic Command Template Identifier'),
                                         name:str = typer.Option(..., help='Command Template Name'),
                                         desc:str = typer.Option(..., help='Command Template Description'),
                                         extAllocCommand:str = typer.Option(None, help='Command Template Extended Allocation Command'),
                                         execScript:str = typer.Option(..., help='Path to executable file for Command Template'),
                                         prepScript:str = typer.Option(None, help='Path to preparation executable script for Command Template or Specific Bash Commands (ml mpi;cp ...)')):
    """Create Command Template from Generic Command Template"""
    try:
        utils.print_and_log("Creating Command Template from Generic Command Template ...")
        body = {
            "_preload_content": False,
            "body": {
                "GenericCommandTemplateId": id, 
                "Name": name,
                "Description": desc,
                "ExtendedAllocationCommand": extAllocCommand,
                "PreparationScript": prepScript,
                "ExecutableFile": execScript,
                "ProjectId": infoCLI.get_hpc_project()["Id"],
                "SessionCode": utils.load_stored_session()
            }
        }

        response = heappeCore.ManagementApi(configuration.get_api_instance()).heappe_management_command_template_from_generic_post(**body)
        jsonData =  json.loads(response.data)
        commandTemplateId= jsonData["Id"]
        utils.print_and_log(f"\nCommand Template was created (Id: {commandTemplateId}):")
        print(json.dumps(jsonData, indent = 3))

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(response_data['title'], response_data['detail'], response_data['status']) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException("HEAppE is not listening on specific address") from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None 
    
    except Exception:
        raise exceptions.Py4HEAppEException(f"Other exception: {exception.message}") from None

@app.command("ModifyFromGeneric")
def modify_command_template_from_generic(id:int = typer.Option(..., help='Command Template Identifier'),
                                         name:str = typer.Option(..., help='Command Template Name'),
                                         desc:str = typer.Option(..., help='Command Template Description'),
                                         extAllocCommand:str = typer.Option(None, help='Command Template Extended Allocation Command'),
                                         execScript:str = typer.Option(..., help='Path to executable file/script for Command Template'),
                                         prepScript:str = typer.Option(None, help='Path to preparation executable script for Command Template or Specific Bash Commands (ml mpi;cp ...)')):
    """Modify Command Template from Generic Command Template"""
    try:
        utils.print_and_log("Modification Command Template from Generic Command Template ...")
        body = {
            "_preload_content": False,
            "body": {
                "CommandTemplateId": id,
                "Name": name,
                "Description": desc,
                "ExtendedAllocationCommand": extAllocCommand,
                "PreparationScript": prepScript,
                "ExecutableFile": execScript,
                "ProjectId": infoCLI.get_hpc_project()["Id"],
                "SessionCode": utils.load_stored_session()
            }
        }

        _ = heappeCore.ManagementApi(configuration.get_api_instance()).heappe_management_command_template_from_generic_put(**body)
        utils.print_and_log(f"\nCommand Template was modified.")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(response_data['title'], response_data['detail'], response_data['status']) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException("HEAppE is not listening on specific address") from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None 
    
    except Exception:
        raise exceptions.Py4HEAppEException(f"Other exception: {exception.message}") from None

@app.command("CreateParameter")
def create_command_template_parameter(uniqueName:str = typer.Option(..., help='Command Template Parameter Identifier (Name)'),
                                     query:str = typer.Option(None, help='Command Template Parameter Query'),
                                     desc:str = typer.Option(..., help='Command Template Parameter Description'),
                                     cmdTemplateId:int = typer.Option(..., help='Command Template Identifier')):
    "Create Command Template Parameter"
    try:
        utils.print_and_log("Creating Command Template Parameter ...")
        body = {
            "_preload_content": False,
            "body": {
                "Identifier": uniqueName,
                "Query": query if query is not None else "",
                "Description": desc,
                "CommandTemplateId": cmdTemplateId,
                "SessionCode": utils.load_stored_session()
            }
        }

        response = heappeCore.ManagementApi(configuration.get_api_instance()).heappe_management_command_template_parameter_post(**body)
        commandTemplateParameterId =  json.loads(response.data)["Id"]
        utils.print_and_log(f"\nCommand Template Parameter was created (Id: {commandTemplateParameterId})")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(response_data['title'], response_data['detail'], response_data['status']) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException("HEAppE is not listening on specific address") from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None 
    
    except Exception:
        raise exceptions.Py4HEAppEException(f"Other exception: {exception.message}") from None

@app.command("ModifyParameter")
def modify_command_template_parameter(id:int = typer.Option(..., help='Command Template Parameter Identifier'),
                                      uniqueName:str = typer.Option(..., help='Command Template Parameter Identifier (Name)'),
                                      query:str = typer.Option(None, help='Command Template Parameter Query'),
                                      desc:str = typer.Option(..., help='Command Template Parameter Description')):
    "Modify Command Template Parameter"
    try:
        utils.print_and_log("Modification Command Template Parameter")
        body = {
            "_preload_content": False,
            "body": {
                "Id": id,
                "Identifier": uniqueName,
                "Query": query if query is not None else "",
                "Description": desc,
                "SessionCode": utils.load_stored_session()
            }
        }

        _ = heappeCore.ManagementApi(configuration.get_api_instance()).heappe_management_command_template_parameter_put(**body)
        utils.print_and_log(f"\nCommand Template Parameter was modified.")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(response_data['title'], response_data['detail'], response_data['status']) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException("HEAppE is not listening on specific address") from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None 
    
    except Exception:
        raise exceptions.Py4HEAppEException(f"Other exception: {exception.message}") from None

@app.command("RemoveParameter")
def remove_command_template_parameter(id:int = typer.Option(..., help='Command Template Parameter Identifier')):
    "Remove Command Template Parameter"
    try:
        utils.print_and_log("Removing Command Template Parameter ...")
        body = {
            "_preload_content": False,
            "body": {
                "Id": id,
                "SessionCode": utils.load_stored_session()
            }
        }

        _ = heappeCore.ManagementApi(configuration.get_api_instance()).heappe_management_command_template_parameter_delete(**body)
        utils.print_and_log("\nCommand Template Parameter was removed.")

    except rest.ApiException as exception:
        try:
            response_data = json.loads(exception.body)
            raise exceptions.Py4HEAppEAPIException(response_data['title'], response_data['detail'], response_data['status']) from None
        except json.JSONDecodeError:
            raise exceptions.Py4HEAppEException("HEAppE is not listening on specific address") from None

    except exceptions.Py4HEAppEAPIInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None

    except exceptions.Py4HEAppEInternalException as exception:
         raise exceptions.Py4HEAppEException(exception.message) from None 
    
    except Exception:
        raise exceptions.Py4HEAppEException(f"Other exception: {exception.message}") from None


if __name__ == '__main__':
    app()