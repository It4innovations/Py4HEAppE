# Py4HEAppE API Client Generation

This guide explains how to re-generate the HEAppE API wrappers for a new HEAppE API version.

Each HEAppE version gets two generated wrappers, both built from the same `swagger.json` and templates:

| Variant | Config file | Generator library | Package |
|:--------|:------------|:------------------|:--------|
| Sync    | `config.json`       | `urllib3` (default) | `py4heappe.heappe_vX.core` |
| Async   | `config_async.json` | `asyncio` (aiohttp) | `py4heappe.heappe_vX.core_async` |

## Steps

1. Obtain the HEAppE OpenAPI definition (for example: `<your-hostname>/swagger/py4heappe/swagger.json`).
2. Update the server URL in `swagger.json`.
3. Replace `Tools/APIWrapperGen/swagger.json` with the new specification.
4. Update `packageName` in both config files:
   - `Tools/APIWrapperGen/config.json`, for example `py4heappe.heappe_vX.core`
   - `Tools/APIWrapperGen/config_async.json`, for example `py4heappe.heappe_vX.core_async` (keep `"library": "asyncio"`)
5. Commit your changes to a branch.
6. Trigger the GitLab pipeline job `API_client_generation`.
7. The pipeline runs OpenAPI Generator (`openapi-generator-cli` v7.26.0) twice in one job, once per config file, using the templates from `Tools/APIWrapperGen/Templates/python`. The job fails if either variant fails to generate.
8. Download the `APIWrapperGen.zip` artifact. It contains one folder per variant:

   ```
   sync/py4heappe/heappe_vX/core/         ->  src/py4heappe/heappe_vX/core/
   async/py4heappe/heappe_vX/core_async/  ->  src/py4heappe/heappe_vX/core_async/
   ```

   Copy only these two leaf packages. Do not copy the generated `py4heappe/__init__.py`, `py4heappe/heappe_vX/__init__.py`, `pyproject.toml`, `setup.py` or `requirements.txt`. The repository's own packaging files are used instead. Also delete the generated `py.typed` marker from the copied `core/` and `core_async/`, as the package does not ship one.
9. Update affected CLI commands and imports for the selected HEAppE version, including `src/py4heappe_cli.py`, `docs/examples/example.py` and `docs/examples/example_async.py`.

## Generating locally

To check template changes without the pipeline, run the same commands locally, writing to the same folder layout as the artifact:

```shell
java -jar openapi-generator-cli-7.26.0.jar generate -i Tools/APIWrapperGen/swagger.json -g python -t Tools/APIWrapperGen/Templates/python/ -o ./_gen/sync  -c Tools/APIWrapperGen/config.json
java -jar openapi-generator-cli-7.26.0.jar generate -i Tools/APIWrapperGen/swagger.json -g python -t Tools/APIWrapperGen/Templates/python/ -o ./_gen/async -c Tools/APIWrapperGen/config_async.json
```

## Hand-written code that survives regeneration

Hand-written code lives in `src/py4heappe/heappe_vX/extensions/`, outside the generated packages, so copying in a fresh `core/` or `core_async/` does not overwrite it:

- `extensions/base/`: CLI exceptions, logger and utilities (used by the sync CLI only).
- `extensions/file_upload.py`: in-memory upload types and helpers shared by both wrappers.
- `extensions/file_transfer_api_ext.py` / `extensions/file_transfer_api_ext_async.py`: `FileTransferApiExt` for the sync and async wrappers.

Check these against the newly generated `FileTransferApi` after regeneration, in case the upload endpoint signature changed.

The one exception is the legacy compatibility shim (`_patch_legacy_api_methods`) at the end of the sync `core/__init__.py`. It is not produced by the templates, so re-apply it after copying a new sync `core/`. The async wrapper does not use it.
