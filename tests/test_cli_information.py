from tests.live_cli_support import LiveCliExampleTestCase


class InformationCliExampleTests(LiveCliExampleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ensure_live_enabled()
        cls.ensure_cli_configured()

    def test_info_version_example(self):
        result = self.run_cli("Info", "Version", extra_env=self.session_env())

        self.assertIn("Version of API:", result.stdout)

    def test_info_cluster_info_example(self):
        result = self.run_cli("Info", "ClusterInfo", extra_env=self.session_env())

        self.assertIn("Cluster information:", result.stdout)

    def test_info_list_params_from_generic_example(self):
        env_values = self.require_env("PY4HEAPPE_TEST_GENERIC_COMMAND_TEMPLATE_ID")
        result = self.run_cli(
            "Info",
            "ListParamsFromGeneric",
            "--id",
            env_values["PY4HEAPPE_TEST_GENERIC_COMMAND_TEMPLATE_ID"],
            "--userScriptPath",
            "run.sh",
            extra_env=self.session_env(),
        )

        self.assertIn("Command template parameters:", result.stdout)

    def test_info_cluster_node_usage_example(self):
        env_values = self.require_env("PY4HEAPPE_TEST_CLUSTER_NODE_TYPE_ID")
        result = self.run_cli(
            "Info",
            "ClusterNodeUsage",
            "--clusterNodeTypeId",
            env_values["PY4HEAPPE_TEST_CLUSTER_NODE_TYPE_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("Cluster node type usage:", result.stdout)
