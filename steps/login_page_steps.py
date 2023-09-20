import time

from pages.login_page import LoginPage
from utils.DriverUtils import DriverUtils


class LoginPageSteps:

    @staticmethod
    def login():
        name = "welcome@artmedia.ge"
        password = "123456"
        login_page = LoginPage()
        time.sleep(2)
        login_page.fill_username(name)
        login_page.fill_password(password)
        login_page.click_login_button()


