from steps.login_page_admin_steps import LoginPageSteps


class TestLoginAdmin:

    def test_login_admin(self):
        login_steps = LoginPageSteps
        login_steps.login()
