# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 2.8.0

### Compatible with HEAppE V6.4.X, V6.3.X, V6.2.X, V6.2.1, V5.0.X, V4.3.X and V4.2.X

### Added
- Added `py4heappe Job InitJobSpecification` to generate minimal JSON job specification template in the current directory or in a user-provided destination.

### Changed
- Expanded `py4heappe Job Create` to accept an optional JSON job specification file and merge CLI overrides on top of values loaded from that file.
- Added optional CLI overrides for the extended HEAppE V6 job specification, including indexed overrides for task attributes and nested collections such as environment variables, template parameter values, required nodes, task parallelization parameters, and task dependencies.
- Switched job specification parsing to build requests from the generated HEAppE V6 models, including generated-model handling for `Priority` and `DependsOn`.
- Replaced the previous `Job Remove` behavior with `Job Delete`, including support for the `--archive-logs` option.

## 2.7.1

### Compatible with HEAppE V6.4.X, V6.3.X, V6.2.X, V6.2.1, V5.0.X, V4.3.X and V4.2.X

### Fixed
- Fixed syntax error (`IndentationError`) in `management_api.py` caused by an empty `if` block for single file upload parameters.
- Fixed the Swagger Codegen mustache template to correctly support single file (`isBinary`), list of files (`items.isBinary`), and regular form parameters.

## 2.7.0

### Compatible with HEAppE V6.4.X, V6.3.X, V6.2.X, V6.2.1, V5.0.X, V4.3.X and V4.2.X

### Changed
- Updated Py4HEAppE wrapper to support new changes in HEAppE V6.4.0 [See HEAppE v6.4.0 CHANGELOG.md](https://github.com/It4innovations/HEAppE/blob/master/CHANGELOG.md#v640)


## 2.6.0

### Compatible with HEAppE V6.3.X, V6.2.X, V6.2.1, V5.0.X, V4.3.X and V4.2.X

### Added

- **File Transfer CLI Commands**: Added full support for the `FileTransfer` HEAppE API suite to manage cluster data channels and job files:
  - `py4heappe FileTransfer Single/Interactive` - Initiates and creates a secure file transfer tunnel via SSH and make a one-time transfer of file(s) or folder (Single) or interactively multiple times (Interactive) (`POST /heappe/FileTransfer/RequestFileTransfer`).
  - Automatically closes an active file transfer tunnel after transfer (`POST /heappe/FileTransfer/CloseFileTransfer`).
  - `py4heappe FileTransfer DownloadParts` - Downloads specific parts of job files from the cluster (`POST /heappe/FileTransfer/DownloadPartsOfJobFilesFromCluster`).
  - `py4heappe FileTransfer ListChanged` - Retrieves a list of all files modified during job execution (`GET /heappe/FileTransfer/ListChangedFilesForJob`).
  - `py4heappe FileTransfer Download` - Downloads a specific individual file directly from the cluster (`POST /heappe/FileTransfer/DownloadFileFromCluster`).
  - `py4heappe FileTransfer Stream` - Uploads files directly into a designated job execution directory (`POST /heappe/FileTransfer/UploadFilesToJobExecutionDir`).

## 2.5.2

### Compatible with HEAppE V6.3.X, V6.2.X, V6.2.1, V5.0.X, V4.3.X and V4.2.X

### Added

- Enhanced `ListAvailableClusters` response with cluster-specific storage paths (`ScratchStoragePath` and `ProjectStoragePath`) for each project.
- Storage paths are now returned in a structured collection `ClusterProjectStoragePaths` within the `ProjectExt` model, including Cluster ID and Name.

## 2.5.1

### Compatible with HEAppE V6.2.X, V6.0.X, V5.0.X, V4.3.X and V4.2.X

### Changed

- Dependencies relaxation.

## 2.5.0

### Compatible with HEAppE V6.2.X, V6.0.X, V5.0.X, V4.3.X and V4.2.X

## 2.4.0

### Compatible with HEAppE V6.1.X, V6.0.X, V5.0.X, V4.3.X and V4.2.X

## V2.3.0

### Compatible with HEAppE V6.0.X, V5.0.X, V4.3.X and V4.2.X

## V2.2.0

### Compatible with HEAppE V5.0.X, V4.3.X and V4.2.X

### Changed

- Update requirements package
- Adding File Commands Groups in CLI (support Job Management)

## V2.1.2

### Compatible with HEAppE V5.0.X, V4.3.X and V4.2.X

### Changed

- Requirements package (python-dotenv)

## V2.1.1

### Compatible with HEAppE V5.0.X, V4.3.X and V4.2.X

### Fixed

- Deserialization response for HEAppE 4.X.X

## V2.1.0

### Compatible with HEAppE V5.0.X, V4.3.X and V4.2.X

## V2.0.0

### Compatible with HEAppE V5.0.X

## V1.0.0

### Compatible with HEAppE V4.2.X and V4.3.X
