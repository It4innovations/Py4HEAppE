from tests.live_cli_support import LiveCliExampleTestCase


class ReportCliExampleTests(LiveCliExampleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ensure_live_enabled()
        cls.ensure_cli_configured()

    def test_report_group_list_example(self):
        result = self.run_cli("Report", "GroupList", extra_env=self.session_env())

        self.assertIn("Associated user groups:", result.stdout)

    def test_report_user_usage_example(self):
        env_values = self.require_env("PY4HEAPPE_TEST_USER_ID")
        result = self.run_cli(
            "Report",
            "UserUsage",
            "--userId",
            env_values["PY4HEAPPE_TEST_USER_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("User usage report:", result.stdout)

    def test_report_group_usage_example(self):
        env_values = self.require_env("PY4HEAPPE_TEST_GROUP_ID")
        result = self.run_cli(
            "Report",
            "GroupUsage",
            "--groupId",
            env_values["PY4HEAPPE_TEST_GROUP_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("User group usage report:", result.stdout)

    def test_report_groups_usage_detailed_example(self):
        result = self.run_cli(
            "Report", "GroupsUsageDetailed", extra_env=self.session_env()
        )

        self.assertIn("Detailed user groups usage report:", result.stdout)

    def test_report_job_usage_example(self):
        env_values = self.require_env("PY4HEAPPE_TEST_REPORT_JOB_ID")
        result = self.run_cli(
            "Report",
            "JobUsage",
            "--id",
            env_values["PY4HEAPPE_TEST_REPORT_JOB_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("Job usage report:", result.stdout)
