from pages.login_page_admin import LoginPage


class LoginPageSteps:
    @staticmethod
    def login():
        email = "welcome@artmedia.ge"
        password = "123456"
        login_page = LoginPage()
        login_page.is_visible()
        login_page.close_php()
        login_page.fill_username(email)
        login_page.fill_password(password)
        login_page.click_login_button()