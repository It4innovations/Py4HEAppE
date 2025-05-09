import json
import os
import time
from io import StringIO
from pathlib import Path

import paramiko
from paramiko import SSHClient
from scp import SCPClient

import py4heappe.heappe_v5.core as hp

configuration = hp.Configuration()
configuration.host = ""
projectIdentificator = ""
username = ""
password = ""
api_instance = hp.ApiClient(configuration)


print(f"Authenticating to HEAppE instance through {username}...")
cred = {
    "_preload_content": False,
    "body": {
        "Credentials": {
            "Username": username,
            "Password": password
        }
    }
}

ulmEndpoint = hp.UserAndLimitationManagementApi(api_instance)
r = ulmEndpoint.heappe_user_and_limitation_management_authenticate_user_password_post(**cred)
session_code = json.loads(r.data)
print(f"Session code: {session_code}")


print("\nFetching HEAppE version info...")
lver_body = {
    "_preload_content": False,
    "SessionCode": session_code
}

manEndpoint = hp.ManagementApi(api_instance)
r = manEndpoint.heappe_management_version_information_get(**lver_body)
r_data = json.loads(r.data)
print(json.dumps(r_data, indent=3))


print("\nFetching cluster info...")
lac_body = {
    "_preload_content": False,
    "SessionCode": session_code
}

ciEndpoint = hp.ClusterInformationApi(api_instance)
r = ciEndpoint.heappe_cluster_information_list_available_clusters_get(**lac_body)
r_data = json.loads(r.data)
print(json.dumps(r_data, indent=3))

print("\nFetching available computational projects...")
lproj_body = {
    "_preload_content": False,
    "SessionCode": session_code,
}

r = ulmEndpoint.heappe_user_and_limitation_management_projects_for_current_user_get(**lproj_body)
r_data = json.loads(r.data)
project = next(f["Project"] for f in r_data if f["Project"]["AccountingString"] == projectIdentificator)
print(json.dumps(project, indent=3))

print("\nCreating job template...")
job_spec_body = {
    "_preload_content": False,
    "body": {
        "JobSpecification": {
            "Name": "job_1",
            #"NotificationEmail": "string",
            #"PhoneNumber": "string",
            #"NotifyOnAbort": true,
            #"NotifyOnFinish": true,
            #"NotifyOnStart": true,
            #"SubProjectIdentifier": "string"
            "ClusterId": 2,
            "FileTransferMethodId": 2,
            "ProjectId": project["Id"],
            "EnvironmentVariables": [],
            "Tasks": [
                {
                    "Name": "task_1",
                    "MinCores": 1,
                    "MaxCores": 128,
                    "Priority": 4,
                    "WalltimeLimit": 600,
                    #"PlacementPolicy": "string"
                    #"RequiredNodes": [
                    #   "string"
                    # ],
                    #"ClusterTaskSubdirectory": "string",
                    #"CpuHyperThreading": true,
                    #"JobArrays": "string",
                    #"IsExclusive": true,
                    #"IsRerunnable": true,
                    #"StandardInputFile": "stdin",
                    "StandardOutputFile": "stdout",
                    "StandardErrorFile": "stderr",
                    "ProgressFile": "stdprog",
                    "LogFile": "stdlog",
                    "ClusterNodeTypeId": 18,
                    "CommandTemplateId": 3,
                    #"TaskParalizationParameters": [
                        #{
                            #"MPIProcesses": 0,
                            #"OpenMPThreads": 0,
                            #"MaxCores": 0
                        #}
                    #],
                    #"EnvironmentVariables": [
                        #{
                            #"Name": "string"
                            #"Value": "string"
                        #}
                    #],
                    #"DependsOn": [
                    #   "string"
                    # ],
                    "TemplateParameterValues": [
                        {
                            "CommandParameterIdentifier": "inputParam",
                            "ParameterValue": "testValue"
                        }
                    ]
                }
            ]
        },
        "SessionCode": session_code
    }
}

jmEndpoint = hp.JobManagementApi(api_instance)
r = jmEndpoint.heappe_job_management_create_job_post(**job_spec_body)
r_data = json.loads(r.data)
job_id = r_data["Id"]
print(f"Job ID: {job_id} ...")


print(f"\nSubmitting job {job_id}...")
submit_body = {
    "_preload_content": False,
    "body": {
        "CreatedJobInfoId": job_id,
        "SessionCode": session_code
    }
}

r = jmEndpoint.heappe_job_management_submit_job_put(**submit_body)
r_data = json.loads(r.data)


print(f"\nWaiting for job {job_id} to finish...")
gcji_body = {
    "_preload_content": False,
    "SubmittedJobInfoId": job_id,
    "SessionCode": session_code
}

while True:
    r = jmEndpoint.heappe_job_management_current_info_for_job_get(**gcji_body)
    r_data = json.loads(r.data)
    state = r_data["State"]
    if r_data["State"] == 16:
        print(f"The job has finished.")
        break
    if r_data["State"] == 32:
        print(f"The job has failed.")
        break
    if r_data["State"] == 64:
        print(f"The job has canceled.")
        break
    print(f"Waiting for job {job_id} to finish... current state: {state}")
    time.sleep(30)


print("\nFetching generated files...")
ft_body = {
    "_preload_content": False,
    "body": {
        "SubmittedJobInfoId": job_id,
        "SessionCode": session_code
    }
}

ftEndpoint = hp.FileTransferApi(api_instance)
r = ftEndpoint.heappe_file_transfer_request_file_transfer_post(**ft_body)
jobtransfer = json.loads(r.data)

lchjf_body = {
    "_preload_content": False,
    "SessionCode": session_code,
    "SubmittedJobInfoId": job_id
}

r = ftEndpoint.heappe_file_transfer_list_changed_files_for_job_get(**lchjf_body)
r_data = json.loads(r.data)
producedFiles = [os.path.normpath(path["FileName"]) for path in r_data]
print(f"Files changed during job execution: {producedFiles}")

print("\nFetching the files...")
ssh = SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
pkey_file = StringIO(jobtransfer["Credentials"]["PrivateKey"])
match jobtransfer["Credentials"]["CipherType"]:
    case 1:
        pkey = paramiko.RSAKey.from_private_key(pkey_file)
    case 2:
        pkey = paramiko.RSAKey.from_private_key(pkey_file)
    case 3:
        pkey = paramiko.ECDSAKey.from_private_key(pkey_file)
    case 4:
        pkey = paramiko.ECDSAKey.from_private_key(pkey_file)
    case default:
        pkey = paramiko.RSAKey.from_private_key(pkey_file)

ssh.connect(jobtransfer["ServerHostname"], username=jobtransfer["Credentials"]["Username"], pkey=pkey)
base_path = jobtransfer["SharedBasepath"]

with SCPClient(ssh.get_transport()) as scp:
    for fn in producedFiles:
        specpath = fn[1:]
        Path(os.path.dirname(f"data_transfer/output/{job_id}/{specpath}")).mkdir(parents=True, exist_ok=True)
        scp.get(os.path.join(base_path, specpath).replace("\\", "/"), f"data_transfer/output/{job_id}/{specpath}")
ssh.close()

ft_body = {
    "_preload_content": False,
    "body": {
        "SubmittedJobInfoId": job_id,
        "PublicKey": jobtransfer["Credentials"]["PublicKey"],
        "SessionCode": session_code
    }
}

ftEndpoint.heappe_file_transfer_download_file_from_cluster_post
r = ftEndpoint.heappe_file_transfer_close_file_transfer_post(**ft_body)
r_data = json.loads(r.data)
print(", ".join(producedFiles) + " fetched")


print("\nFetching resource usage report...")
rur_body = {
    "_preload_content": False,
    "SessionCode": session_code,
    "JobId": job_id
}

jrEndpoint = hp.JobReportingApi(api_instance)
r = jrEndpoint.heappe_job_reporting_resource_usage_report_for_job_get(**rur_body)
r_data = json.loads(r.data)
usedResources = r_data["TotalUsage"]
print(f"Job {job_id} used {usedResources} resources...")


print(f"\nRemoving job {job_id}...")
ft_body = {
    "_preload_content": False,
    "body": {
        "SubmittedJobInfoId": job_id,
        "SessionCode": session_code
    }
}

r = jmEndpoint.heappe_job_management_delete_job_delete(**ft_body)
r_data = json.loads(r.data)
print(r_data)
