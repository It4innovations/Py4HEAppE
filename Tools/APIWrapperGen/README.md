# Py4HEAppE API Client Generation

The content contains how to re-generate the HEAppE API wrapper with the new version of the HEAppE API

## Steps

1. Obtain HEAppE API Swagger definition **(eg.http://localhost:5000/swagger/py4heappe/swagger.json)**
2. Update server url in swagger.json file to <http://localhost:5000>
3. Upload the downloaded Swagger definition and replace it in repository folder **'Tools\APIWrapperGen\swagger.json'**
4. Modify packageName (change version) in file **'Tools\APIWrapperGen\config.json' (packageName: "py4heappe.heappe_v\*.core)**
5. Commit into random branch (not into develop or main)
6. Manually triggered pipeline for the API wrapper generation
7. Download pipeline artefact and put files in **'src\py4heappe\core\version'**
8. Modify Py4HEAppE CLI affected commands and imports to specific version
9. Modify import to specific version in **'docs\examples\example.py'**
