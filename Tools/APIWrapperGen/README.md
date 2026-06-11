# Py4HEAppE API Client Generation

The content contains how to re-generate the HEAppE API wrapper with the new version of the HEAppE API

## Steps

1. Obtain HEAppE API Swagger definition **(eg.<your-hostname>/swagger/py4heappe/swagger.json)** for example
2. Update server url in swagger.json file to <your-hostname>
3. Replace old swagger.json file with the new one in repository location **'Tools\APIWrapperGen\swagger.json'**
4. Modify packageName (change version) in repository location **'Tools\APIWrapperGen\config.json' (packageName: "py4heappe.heappe_v\*.core)**
5. Commit into any random branch
6. In GitHub/GitLab, trigger your pipeline for the API wrapper generation
7. Download pipeline artefact and put files in **'src\py4heappe\<heappe-version>\core'**
8. Modify Py4HEAppE CLI affected commands as well as any imports to use specific heappe version
9. Modify import to specific version in **'docs\examples\example.py'**, and in **'src\py4heappe_cli.py'**.
