import time

from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
from pages.base_form import BaseForm


class WordCodePage(BaseForm):
    __word_codes_button = Button(By.XPATH, "//a[contains(text(),'სიტყვა-კოდები')]", "sityva kodebi")
    __add_new_word_code = Button(By.XPATH, "//button[@class='_AppButton_1k2x1_1 _AppButton--Green_1k2x1_88']", "axlis damateba")
    __word_codes_list = Button(By.XPATH, "//div[@class='_AppSortingList__Wrapper__List__Item_6ohc1_45']//span[position()=1]", "sityva kodebis listi")
    __word_codes_list_for_delete = Button(By.XPATH, "//div[@class='_AppSortingList__Wrapper__List__Item_6ohc1_45']//span[@data-test='delete']", "sityva kodebis listi")
    __delate_button = Button(By.XPATH, "//button[.='წაშლა']", "waslis dadastureba")
    def __init__(self):
        super().__init__(By.XPATH, "//button[@class='_AppButton_1k2x1_1 _AppButton--Green_1k2x1_88']", "login button")

    def click_word_codes_button(self):
        self.__word_codes_button.click()

    def click_new_word_code_button(self):
        self.__add_new_word_code.click()

    def get_last_word_code(self):
        return self.__word_codes_list.find_elements()

    def get_last_word_for_delete(self):
        return self.__word_codes_list_for_delete.find_elements()

    def del_button_click(self):
        self.__delate_button.click()