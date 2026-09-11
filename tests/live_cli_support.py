import os
import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
CLI_CONFIG_PATH = SRC_DIR / "py4heappe" / "heappe_v6" / "cli" / ".env"

LIVE_FLAG = "PY4HEAPPE_RUN_LIVE_CLI_TESTS"
MUTATING_FLAG = "PY4HEAPPE_TEST_RUN_MUTATING_COMMANDS"
SESSION_CODE_ENV = "PY4HEAPPE_TEST_SESSION_CODE"


def _set_or_remove_env_var(env, key, value):
    matching_keys = [existing_key for existing_key in env if existing_key.lower() == key.lower()]
    for matching_key in matching_keys:
        env.pop(matching_key, None)

    if value is not None:
        env[key] = value


def run_py4heappe_command(args, *, input_text=None, extra_env=None):
    env = os.environ.copy()
    python_path = env.get("PYTHONPATH")
    env["PYTHONPATH"] = (
        str(SRC_DIR) if not python_path else f"{SRC_DIR}{os.pathsep}{python_path}"
    )
    env["PYTHONIOENCODING"] = "utf-8"

    for key, value in (extra_env or {}).items():
        _set_or_remove_env_var(env, key, value)

    return subprocess.run(
        [sys.executable, "-m", "py4heappe_cli", *args],
        cwd=REPO_ROOT,
        input=input_text,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    )


class LiveCliExampleTestCase(unittest.TestCase):
    _config_existed: bool = False
    _config_content: str = ""
    _cli_configured: bool = False

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._config_existed = CLI_CONFIG_PATH.exists()
        if cls._config_existed:
            cls._config_content = CLI_CONFIG_PATH.read_text(encoding="utf-8")
        else:
            cls._config_content = ""
        cls._cli_configured = False

    @classmethod
    def tearDownClass(cls):
        try:
            if cls._config_existed:
                CLI_CONFIG_PATH.write_text(cls._config_content, encoding="utf-8")
            elif CLI_CONFIG_PATH.exists():
                CLI_CONFIG_PATH.unlink()
        finally:
            super().tearDownClass()

    @classmethod
    def ensure_live_enabled(cls):
        if os.environ.get(LIVE_FLAG) != "1":
            raise AssertionError(
                f"Set {LIVE_FLAG}=1 to run live CLI example tests."
            )

    @classmethod
    def ensure_mutating_commands_enabled(cls):
        if os.environ.get(MUTATING_FLAG) != "1":
            raise AssertionError(
                f"Set {MUTATING_FLAG}=1 to run mutating CLI example tests."
            )

    @classmethod
    def require_env(cls, *names):
        missing = [name for name in names if not os.environ.get(name)]
        if missing:
            raise AssertionError(
                "Missing required environment variable(s): "
                + ", ".join(missing)
            )
        return {name: os.environ[name] for name in names}

    @classmethod
    def session_env(cls):
        return {"sessionCode": cls.require_env(SESSION_CODE_ENV)[SESSION_CODE_ENV]}

    @classmethod
    def ensure_cli_configured(cls):
        if cls._cli_configured:
            return

        env_values = cls.require_env("PY4HEAPPE_TEST_URL", "PY4HEAPPE_TEST_PROJECT")
        if CLI_CONFIG_PATH.exists():
            CLI_CONFIG_PATH.unlink()

        result = run_py4heappe_command(
            ["Conf", "Init"],
            input_text=(
                f"{env_values['PY4HEAPPE_TEST_URL']}\n"
                f"{env_values['PY4HEAPPE_TEST_PROJECT']}\n"
                f"{env_values['PY4HEAPPE_TEST_PROJECT']}\n"
            ),
            extra_env={"url": None, "project": None},
        )
        cls.assert_command_succeeded(result, ["Conf", "Init"])
        cls._cli_configured = True

    @staticmethod
    def split_env_list(name):
        raw_value = os.environ.get(name, "")
        return [item.strip() for item in raw_value.split(";") if item.strip()]

    @staticmethod
    def append_repeated_option(args, option_name, values):
        for value in values:
            args.extend([option_name, value])

    @classmethod
    def assert_command_succeeded(cls, result, args):
        if result.returncode == 0:
            return

        formatted_command = " ".join(args)
        raise AssertionError(
            f"Command failed: py4heappe {formatted_command}\n"
            f"exit code: {result.returncode}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )

    def run_cli(self, *args, input_text=None, extra_env=None):
        result = run_py4heappe_command(
            list(args), input_text=input_text, extra_env=extra_env
        )
        self.assert_command_succeeded(result, list(args))
        return result
