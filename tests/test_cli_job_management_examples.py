import tempfile
import uuid
from pathlib import Path

from tests.live_cli_support import LiveCliExampleTestCase


class JobManagementCliExampleTests(LiveCliExampleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ensure_live_enabled()
        cls.ensure_cli_configured()

    def test_job_init_job_specification_example(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "job_specification.json"
            result = self.run_cli(
                "Job",
                "InitJobSpecification",
                "--file-destination",
                str(file_path),
            )

            self.assertIn("job specification was created in:", result.stdout)
            self.assertTrue(file_path.exists())

    def test_job_create_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env(
            "PY4HEAPPE_TEST_JOB_SPEC_FILE",
            "PY4HEAPPE_TEST_SESSION_CODE",
        )
        result = self.run_cli(
            "Job",
            "Create",
            "--json-job-spec-file",
            env_values["PY4HEAPPE_TEST_JOB_SPEC_FILE"],
            "--session-code",
            env_values["PY4HEAPPE_TEST_SESSION_CODE"],
            "--name",
            f"py4heappe-cli-job-{uuid.uuid4().hex[:8]}",
        )

        self.assertIn("HPC job was created", result.stdout)

    def test_job_submit_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env("PY4HEAPPE_TEST_SUBMIT_JOB_ID")
        result = self.run_cli(
            "Job",
            "Submit",
            "--id",
            env_values["PY4HEAPPE_TEST_SUBMIT_JOB_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("HPC job was submitted successfully.", result.stdout)

    def test_job_cancel_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env("PY4HEAPPE_TEST_CANCEL_JOB_ID")
        result = self.run_cli(
            "Job",
            "Cancel",
            "--id",
            env_values["PY4HEAPPE_TEST_CANCEL_JOB_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("HPC job was cancelled.", result.stdout)

    def test_job_delete_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env("PY4HEAPPE_TEST_DELETE_JOB_ID")
        result = self.run_cli(
            "Job",
            "Delete",
            "--id",
            env_values["PY4HEAPPE_TEST_DELETE_JOB_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("HPC job was deleted successfully.", result.stdout)

    def test_job_list_example(self):
        result = self.run_cli("Job", "List", extra_env=self.session_env())

        self.assertIn("HPC jobs:", result.stdout)

    def test_job_info_example(self):
        env_values = self.require_env("PY4HEAPPE_TEST_INFO_JOB_ID")
        result = self.run_cli(
            "Job",
            "Info",
            "--id",
            env_values["PY4HEAPPE_TEST_INFO_JOB_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("HPC job info:", result.stdout)

    def test_job_copy_data_to_temp_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env(
            "PY4HEAPPE_TEST_COPY_TO_TEMP_JOB_ID",
            "PY4HEAPPE_TEST_COPY_TO_TEMP_PATH",
        )
        result = self.run_cli(
            "Job",
            "CopyDataToTemp",
            "--id",
            env_values["PY4HEAPPE_TEST_COPY_TO_TEMP_JOB_ID"],
            "--path",
            env_values["PY4HEAPPE_TEST_COPY_TO_TEMP_PATH"],
            extra_env=self.session_env(),
        )

        self.assertIn("copied to temporary location", result.stdout)

    def test_job_copy_data_from_temp_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env(
            "PY4HEAPPE_TEST_COPY_FROM_TEMP_JOB_ID",
            "PY4HEAPPE_TEST_TEMP_SESSION_CODE",
        )
        result = self.run_cli(
            "Job",
            "CopyDataFromTemp",
            "--id",
            env_values["PY4HEAPPE_TEST_COPY_FROM_TEMP_JOB_ID"],
            "--temporaryHash",
            env_values["PY4HEAPPE_TEST_TEMP_SESSION_CODE"],
            extra_env=self.session_env(),
        )

        self.assertIn("Copying HPC job data from temporary location", result.stdout)

    def test_job_get_allocated_nodes_example(self):
        env_values = self.require_env("PY4HEAPPE_TEST_SUBMITTED_TASK_ID")
        result = self.run_cli(
            "Job",
            "GetAllocatedNodes",
            "--taskId",
            env_values["PY4HEAPPE_TEST_SUBMITTED_TASK_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("uses the following nodes", result.stdout)
