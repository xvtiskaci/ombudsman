from selenium.webdriver.common.by import By
from elements.button import Button
from elements.input import Input
from pages.base_form import BaseForm


class LoginPage(BaseForm):
    __username = Input(By.XPATH, "//input[@id='email']", "email")
    __password = Input(By.XPATH, "//input[@id='password']", "password")
    __login_button = Button(By.XPATH, "//button[@class='gilaki']", "login")
    __close_php_button = Button(By.XPATH, "//a[@class='phpdebugbar-close-btn']", "გაითიშოს ქვედა გამოშლილი პჰპ")

    def __init__(self):
        super().__init__(By.XPATH, "//div[@class='logo']//*[name()='svg']", "login button")

    def close_php(self):
        self.__close_php_button.click()

    def fill_username(self, email):
        self.__username.send_text(email)

    def fill_password(self, password):
        self.__password.send_text(password)

    def click_login_button(self):
        self.__login_button.click()