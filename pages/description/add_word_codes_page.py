from selenium.webdriver.common.by import By

from elements.button import Button
from elements.input import Input
from pages.base_form import BaseForm


class AddWordCodePage(BaseForm):
    __fill_word_code_name = Input(By.XPATH, "//input[@placeholder='დასახელება']", "sityva kodis saxelis shevseba")
    __clear_and_fill_name = Input(By.XPATH, "//input", "gasuftaveba")
    __click_add_word_code_name_button = Button(By.XPATH, "//button[@class='_AppButton_1k2x1_1 _AppButton--FullWidth_1k2x1_61']", "damatebis gilaki")

    def __init__(self):
        super().__init__(By.XPATH, "//div[.='უკან დაბრუნება']", "login button")

    def fill_word_code_name(self, value):
        self.__fill_word_code_name.send_text(value)

    def redact_fill_word_code_name(self, value):
        self.__clear_and_fill_name.clear_and_fill(value)


    def click_add_word_code_name_button(self):
        self.__click_add_word_code_name_button.click()