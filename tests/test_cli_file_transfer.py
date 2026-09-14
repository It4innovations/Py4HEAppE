import tempfile
from pathlib import Path

from tests.live_cli_support import LiveCliExampleTestCase


class FileTransferCliExampleTests(LiveCliExampleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ensure_live_enabled()
        cls.ensure_cli_configured()

    def test_file_transfer_single_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env("PY4HEAPPE_TEST_SINGLE_TRANSFER_JOB_ID")
        task_id = self.split_env_list("PY4HEAPPE_TEST_SINGLE_TRANSFER_TASK_ID")

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "single-upload.txt"
            file_path.write_text("py4heappe single upload example", encoding="utf-8")

            args = [
                "FileTransfer",
                "Single",
                "--id",
                env_values["PY4HEAPPE_TEST_SINGLE_TRANSFER_JOB_ID"],
            ]
            if task_id:
                args.extend(["--taskId", task_id[0]])
            args.extend(["--files", str(file_path)])

            result = self.run_cli(*args, extra_env=self.session_env())

        self.assertIn("Requesting file transfer tunnel", result.stdout)

    def test_file_transfer_interactive_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env("PY4HEAPPE_TEST_INTERACTIVE_TRANSFER_JOB_ID")
        task_id = self.split_env_list("PY4HEAPPE_TEST_INTERACTIVE_TRANSFER_TASK_ID")

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "interactive-upload.txt"
            file_path.write_text(
                "py4heappe interactive upload example", encoding="utf-8"
            )

            args = [
                "FileTransfer",
                "Interactive",
                "--id",
                env_values["PY4HEAPPE_TEST_INTERACTIVE_TRANSFER_JOB_ID"],
            ]
            if task_id:
                args.extend(["--taskId", task_id[0]])

            result = self.run_cli(
                *args,
                input_text=f"{file_path}\nq\n",
                extra_env=self.session_env(),
            )

        self.assertIn("Requesting interactive file transfer tunnel", result.stdout)

    def test_file_transfer_download_example(self):
        env_values = self.require_env(
            "PY4HEAPPE_TEST_DOWNLOAD_JOB_ID",
            "PY4HEAPPE_TEST_DOWNLOAD_RELATIVE_FILE_PATH",
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            result = self.run_cli(
                "FileTransfer",
                "Download",
                "--id",
                env_values["PY4HEAPPE_TEST_DOWNLOAD_JOB_ID"],
                "--relativeFilePath",
                env_values["PY4HEAPPE_TEST_DOWNLOAD_RELATIVE_FILE_PATH"],
                "--download-file-path",
                temp_dir,
                extra_env=self.session_env(),
            )

        self.assertIn("Downloaded file was written to:", result.stdout)

    def test_file_transfer_download_parts_example(self):
        env_values = self.require_env("PY4HEAPPE_TEST_DOWNLOAD_PARTS_JOB_ID")
        task_file_offsets = self.split_env_list("PY4HEAPPE_TEST_TASK_FILE_OFFSETS")
        if not task_file_offsets:
            raise self.skipTest("Missing required environment variable: PY4HEAPPE_TEST_TASK_FILE_OFFSETS")

        with tempfile.TemporaryDirectory() as temp_dir:
            args = [
                "FileTransfer",
                "DownloadParts",
                "--id",
                env_values["PY4HEAPPE_TEST_DOWNLOAD_PARTS_JOB_ID"],
            ]
            self.append_repeated_option(args, "--taskFileOffset", task_file_offsets)
            args.extend(["--download-directory-path", temp_dir])

            result = self.run_cli(*args, extra_env=self.session_env())

        self.assertIn("Downloaded files were written to:", result.stdout)

    def test_file_transfer_list_changed_example(self):
        env_values = self.require_env("PY4HEAPPE_TEST_LIST_CHANGED_JOB_ID")
        result = self.run_cli(
            "FileTransfer",
            "ListChanged",
            "--id",
            env_values["PY4HEAPPE_TEST_LIST_CHANGED_JOB_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("Changed files:", result.stdout)

    def test_file_transfer_stream_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env("PY4HEAPPE_TEST_STREAM_JOB_ID")
        task_id = self.split_env_list("PY4HEAPPE_TEST_STREAM_TASK_ID")

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "stream-upload.txt"
            file_path.write_text("py4heappe stream upload example", encoding="utf-8")

            args = [
                "FileTransfer",
                "Stream",
                "--id",
                env_values["PY4HEAPPE_TEST_STREAM_JOB_ID"],
            ]
            if task_id:
                args.extend(["--taskId", task_id[0]])
            args.extend(["--files", str(file_path)])

            result = self.run_cli(*args, extra_env=self.session_env())

        self.assertIn("Upload results:", result.stdout)
