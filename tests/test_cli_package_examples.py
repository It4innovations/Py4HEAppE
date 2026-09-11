import unittest


class CliPackageExampleTests(unittest.TestCase):
    def test_cli_package_init_has_no_runnable_commands(self):
        self.skipTest(
            "src\\py4heappe\\heappe_v6\\cli\\__init__.py does not expose runnable CLI commands; the composed root CLI lives in src\\py4heappe_cli.py."
        )
