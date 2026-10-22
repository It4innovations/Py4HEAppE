# Py4HEAppE API Client Generation

This guide explains how to re-generate the HEAppE API wrapper for a new HEAppE API version.

## Steps

1. Obtain the HEAppE OpenAPI definition (for example: `<your-hostname>/swagger/py4heappe/swagger.json`).
2. Update the server URL in `swagger.json`.
3. Replace `Tools/APIWrapperGen/swagger.json` with the new specification.
4. Update `packageName` in `Tools/APIWrapperGen/config.json` (for example `py4heappe.heappe_v*.core`).
5. Commit your changes to a branch.
6. Trigger the GitLab pipeline job `API_client_generation`.
7. The pipeline uses OpenAPI Generator (`openapi-generator-cli` v7.26.0) with templates from `Tools/APIWrapperGen/Templates/python`.
8. Download `APIWrapperGen.zip` artifact and copy generated files into `src/py4heappe/<heappe-version>/core`.
9. Update affected CLI commands/imports for the selected HEAppE version, including `docs/examples/example.py` and `src/py4heappe_cli.py`.
