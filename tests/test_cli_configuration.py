import os

from tests.live_cli_support import CLI_CONFIG_PATH, LiveCliExampleTestCase


class ConfigurationCliExampleTests(LiveCliExampleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ensure_live_enabled()

    def test_conf_init_example(self):
        env_values = self.require_env("PY4HEAPPE_TEST_URL", "PY4HEAPPE_TEST_PROJECT")
        if CLI_CONFIG_PATH.exists():
            CLI_CONFIG_PATH.unlink()

        result = self.run_cli(
            "Conf",
            "Init",
            input_text=(
                f"{env_values['PY4HEAPPE_TEST_URL']}\n"
                f"{env_values['PY4HEAPPE_TEST_PROJECT']}\n"
                f"{env_values['PY4HEAPPE_TEST_PROJECT']}\n"
            ),
            extra_env={"url": None, "project": None},
        )

        self.assertIn("Py4HEAppE is configured.", result.stdout)
        self.assertTrue(CLI_CONFIG_PATH.exists())
