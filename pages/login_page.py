from selenium.webdriver.common.by import By

from elements.button import Button
from elements.input import Input
from pages.base_form import BaseForm


class LoginPage:
    __username = Input(By.XPATH, "//input[@placeholder='მომხმარებელი']", "username")
    __password = Input(By.XPATH, "//input[@placeholder='პაროლი']", "password")
    __login_button = Button(By.XPATH, "//div[@class='_AppButton__Round__Wrapper_16gsi_13']", "login button")

    def fill_username(self, name):
        self.__username.send_text(name)

    def fill_password(self, password):
        self.__password.send_text(password)

    def click_login_button(self):
        self.__login_button.click()
