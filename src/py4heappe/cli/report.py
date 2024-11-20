import json
import typer

import py4heappe.cli.configuration as configuration
import py4heappe.core.base.utils as utils
import py4heappe.core as heappeCore

from datetime import datetime
from py4heappe.core.base import exceptions
from py4heappe.core  import rest 


app = typer.Typer(name="ReportCLI", no_args_is_help=True, pretty_exceptions_show_locals=False)

@app.command(name="GroupList")
def list_groups():
    """List groups where the user is assigned"""
    try:
        utils.print_and_log("Listing groups where the user is assigned ...") 
        parameters = {
            "_preload_content": False,
            "SessionCode": utils.load_stored_session()
        }

        response = heappeCore.JobReportingApi(configuration.get_api_instance()).heappe_job_reporting_list_adaptor_user_groups_get(**parameters)
        print(f"\nAssigned Groups:\n{json.dumps(json.loads(response.data), indent = 3)}")

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

@app.command(name="UserUsage")
def get_user_report(userId:int = typer.Option(..., help='User Identifier'),
                    startDate:str = typer.Option(None, help='Start Date with time (Format: YYYY-MM-DDTHH:mm:ss)'),
                    endDate:str = typer.Option(None, help='End Date with time (Format:YYYY-MM-DDTHH:mm:ss)')):
    """Get user report for his jobs"""
    try:
        utils.print_and_log("Getting user report for his jobs ...") 
        parameters = {
            "_preload_content": False,
            "UserId": userId,
            "StartTime": startDate if startDate is not None else "2000-01-01T00:00:00Z",
            "EndTime": endDate if endDate is not None else datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "SessionCode": utils.load_stored_session()
        }

        response = heappeCore.JobReportingApi(configuration.get_api_instance()).heappe_job_reporting_user_resource_usage_report_get(**parameters)
        print(f"\nUser Report:\n{json.dumps(json.loads(response.data), indent = 3)}")
       
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

@app.command(name="GroupUsage")
def get_group_report(groupId:int = typer.Option(..., help='Group Identifier'),
                     startDate:str = typer.Option(None, help='Start Date with time (Format: YYYY-MM-DDTHH:mm:ss)'),
                     endDate:str = typer.Option(None, help='End Date with time (Format:YYYY-MM-DDTHH:mm:ss)')):
    """Get group report for group jobs"""
    try:
        utils.print_and_log("Getting group report for group jobs ...") 
        parameters = {
            "_preload_content": False,
            "GroupId": groupId,
            "StartTime": startDate if startDate is not None else "2000-01-01T00:00:00Z",
            "EndTime": endDate if endDate is not None else datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "SessionCode": utils.load_stored_session()
        }

        response = heappeCore.JobReportingApi(configuration.get_api_instance()).heappe_job_reporting_user_group_resource_usage_report_get(**parameters)
        print(f"\nGroup Report:\n{json.dumps(json.loads(response.data), indent = 3)}")
       
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

@app.command(name="GroupUsageDetailed")
def get_detailed_jobs_report():
    """Get detailed report for all group jobs"""
    try:
        utils.print_and_log("Getting detailed report for all group jobs ...") 
        parameters = {
            "_preload_content": False,
            "SessionCode": utils.load_stored_session()
        }

        response = heappeCore.JobReportingApi(configuration.get_api_instance()).heappe_job_reporting_jobs_detailed_report_get(**parameters)
        print(f"\nJobs Report:\n{json.dumps(json.loads(response.data), indent = 3)}")

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

@app.command(name="UserJobUsage")
def get_detailed_job_report(id:int = typer.Option(..., help='HPC Job Info Identifier')):
    """Get detailed report for a user specific job"""
    try:
        utils.print_and_log("Getting detailed report for a user specific job ...") 
        parameters = {
            "_preload_content": False,
            "JobId": id,
            "SessionCode": utils.load_stored_session()
        }

        response = heappeCore.JobReportingApi(configuration.get_api_instance()).heappe_job_reporting_resource_usage_report_for_job_get(**parameters)
        print(f"\nJob Report:\n{json.dumps(json.loads(response.data), indent = 3)}")

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