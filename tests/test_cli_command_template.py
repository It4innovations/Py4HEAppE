import uuid

from tests.live_cli_support import LiveCliExampleTestCase


class CommandTemplateCliExampleTests(LiveCliExampleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ensure_live_enabled()
        cls.ensure_cli_configured()

    def test_cmdtemp_list_example(self):
        result = self.run_cli("CmdTemp", "List", extra_env=self.session_env())

        self.assertIn("List of command templates", result.stdout)

    def test_cmdtemp_create_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env("PY4HEAPPE_TEST_CLUSTER_NODE_TYPE_ID")
        template_name = f"py4heappe-cli-example-{uuid.uuid4().hex[:8]}"
        result = self.run_cli(
            "CmdTemp",
            "Create",
            "--Name",
            template_name,
            "--desc",
            "CLI example command template",
            "--execScript",
            "run.sh",
            "--clusterNodeTypeId",
            env_values["PY4HEAPPE_TEST_CLUSTER_NODE_TYPE_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("Command template was created", result.stdout)

    def test_cmdtemp_modify_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env(
            "PY4HEAPPE_TEST_MODIFY_COMMAND_TEMPLATE_ID",
            "PY4HEAPPE_TEST_CLUSTER_NODE_TYPE_ID",
        )
        result = self.run_cli(
            "CmdTemp",
            "Modify",
            "--id",
            env_values["PY4HEAPPE_TEST_MODIFY_COMMAND_TEMPLATE_ID"],
            "--Name",
            "py4heappe-cli-modified-template",
            "--desc",
            "Updated by CLI example test",
            "--execScript",
            "run.sh",
            "--clusterNodeTypeId",
            env_values["PY4HEAPPE_TEST_CLUSTER_NODE_TYPE_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("Command template was modified.", result.stdout)

    def test_cmdtemp_remove_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env("PY4HEAPPE_TEST_REMOVE_COMMAND_TEMPLATE_ID")
        result = self.run_cli(
            "CmdTemp",
            "Remove",
            "--id",
            env_values["PY4HEAPPE_TEST_REMOVE_COMMAND_TEMPLATE_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("Command template was removed.", result.stdout)

    def test_cmdtemp_create_from_generic_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env("PY4HEAPPE_TEST_GENERIC_COMMAND_TEMPLATE_ID")
        template_name = f"py4heappe-cli-generic-{uuid.uuid4().hex[:8]}"
        result = self.run_cli(
            "CmdTemp",
            "CreateFromGeneric",
            "--id",
            env_values["PY4HEAPPE_TEST_GENERIC_COMMAND_TEMPLATE_ID"],
            "--name",
            template_name,
            "--desc",
            "CLI example generic template",
            "--execScript",
            "run.sh",
            extra_env=self.session_env(),
        )

        self.assertIn("Command template was created", result.stdout)

    def test_cmdtemp_modify_from_generic_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env(
            "PY4HEAPPE_TEST_MODIFY_FROM_GENERIC_COMMAND_TEMPLATE_ID"
        )
        result = self.run_cli(
            "CmdTemp",
            "ModifyFromGeneric",
            "--id",
            env_values["PY4HEAPPE_TEST_MODIFY_FROM_GENERIC_COMMAND_TEMPLATE_ID"],
            "--name",
            "py4heappe-cli-generic-modified",
            "--desc",
            "Updated by CLI example test",
            "--execScript",
            "run.sh",
            extra_env=self.session_env(),
        )

        self.assertIn("Command template was modified.", result.stdout)

    def test_cmdtemp_list_parameter_example(self):
        env_values = self.require_env("PY4HEAPPE_TEST_COMMAND_TEMPLATE_PARAMETER_ID")
        result = self.run_cli(
            "CmdTemp",
            "ListParameter",
            "--id",
            env_values["PY4HEAPPE_TEST_COMMAND_TEMPLATE_PARAMETER_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("Command template parameter:", result.stdout)

    def test_cmdtemp_create_parameter_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env("PY4HEAPPE_TEST_CREATE_PARAMETER_COMMAND_TEMPLATE_ID")
        parameter_name = f"py4heappe_param_{uuid.uuid4().hex[:8]}"
        result = self.run_cli(
            "CmdTemp",
            "CreateParameter",
            "--uniqueName",
            parameter_name,
            "--desc",
            "CLI example command template parameter",
            "--cmdTemplateId",
            env_values["PY4HEAPPE_TEST_CREATE_PARAMETER_COMMAND_TEMPLATE_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("Command template parameter was created", result.stdout)

    def test_cmdtemp_modify_parameter_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env("PY4HEAPPE_TEST_MODIFY_PARAMETER_ID")
        result = self.run_cli(
            "CmdTemp",
            "ModifyParameter",
            "--id",
            env_values["PY4HEAPPE_TEST_MODIFY_PARAMETER_ID"],
            "--uniqueName",
            "py4heappe_param_modified",
            "--desc",
            "Updated by CLI example test",
            extra_env=self.session_env(),
        )

        self.assertIn("Command template parameter was modified.", result.stdout)

    def test_cmdtemp_remove_parameter_example(self):
        self.ensure_mutating_commands_enabled()
        env_values = self.require_env("PY4HEAPPE_TEST_REMOVE_PARAMETER_ID")
        result = self.run_cli(
            "CmdTemp",
            "RemoveParameter",
            "--id",
            env_values["PY4HEAPPE_TEST_REMOVE_PARAMETER_ID"],
            extra_env=self.session_env(),
        )

        self.assertIn("Command template parameter was removed.", result.stdout)
