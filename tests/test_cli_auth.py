from tests.live_cli_support import LiveCliExampleTestCase


class AuthCliExampleTests(LiveCliExampleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ensure_live_enabled()
        cls.ensure_cli_configured()

    def test_auth_userpass_example(self):
        env_values = self.require_env("CREDENTIALS_USERNAME", "CREDENTIALS_PASSWORD")
        result = self.run_cli("Auth", "UserPass", extra_env=env_values,
                input_text=(
                f"{env_values['CREDENTIALS_USERNAME']}\n"
                f"{env_values['CREDENTIALS_PASSWORD']}\n"
            ),)

        self.assertIn("User was authenticated.", result.stdout)

    # def test_auth_openid_example(self):
    #     env_values = self.require_env("CREDENTIALS_TOKEN")
    #     result = self.run_cli("Auth", "OpenId", extra_env=env_values)
    #
    #     self.assertIn("User was authenticated.", result.stdout)
