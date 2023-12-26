from selenium.webdriver.common.by import By

from elements.button import Button
from elements.input import Input
from pages.base_form import BaseForm


class LoginPage(BaseForm):
    __username = Input(By.XPATH, "//input[@placeholder='მომხმარებელი']", "username")
    __password = Input(By.XPATH, "//input[@placeholder='პაროლი']", "password")
    __login_button = Button(By.XPATH, "//button[@class='_AppButton_1k2x1_1 _AppButton--FullWidth_1k2x1_61']", "login button")

    def __init__(self):
        super().__init__(By.XPATH, "//button[@class='_AppButton_1k2x1_1 _AppButton--FullWidth_1k2x1_61']", "login button")

    def fill_username(self, name):
        self.__username.send_text(name)

    def fill_password(self, password):
        self.__password.send_text(password)

    def click_login_button(self):
        self.__login_button.click()
