from steps.gverdebi_steps import GverdebiPageSteps
from steps.login_page_admin_steps import LoginPageSteps


class TestMenu:

    def test_translate(self):
        login_steps = LoginPageSteps
        login_steps.login()
        pages_steps = GverdebiPageSteps
        pages_steps.gverdebi_page_steps()
