from selenium.webdriver.common.by import By

from elements.button import Button
from elements.input import Input
from pages.base_form import BaseForm


class GverdebiPage(BaseForm):
    __pages_button = Button(By.XPATH, "//a[@title='გვერდები']", "გვერდების მენიუ")
    __add_new_button = Button(By.XPATH, "//div[@class='add']", "ახლის დამატების ღილაკი")
    __head_name = Input(By.XPATH, "//input[@id='title']", "სათაურის ველი")
    __add_button = Button(By.XPATH, "//button[@class='gilaki']", "დამატების ღილაკი")
    __edits_buttons_list = Button(By.XPATH, "//li[@class='edit']//a", "დამატებული გვერდის ედითის ღილაკი")
    __back = Button(By.XPATH, "//div[@class='back_to']", "უკან გამოსვლა")
    __delete_buttons_list = Button(By.XPATH, "//li[@class='delete']//a", "დარედაქტირებული გვერდის წაშლის ღილაკი")
    __confirm_delete = Button(By.XPATH, "//button[@class='gilaki yes']", "წაშლის დადასტურება")

    def __init__(self):
        super().__init__(By.XPATH, "//h1[@class='title']//span[contains(text(),'გვერდები')]",
                         "გვერდების დასახელება ზედა მარცხენა კუთხეში")

    def click_pages_menu(self):
        self.__pages_button.click()

    def click_add_new_button(self):
        self.__add_new_button.click()

    def fill_head_name(self, value):
        self.__head_name.send_text(value)

    def click_add_button(self):
        self.__add_button.click()

    def find_edit_button(self):
        return self.__edits_buttons_list.find_elements()

    def redact_head_name(self, red_value):
        self.__head_name.clear_and_fill(red_value)

    def click_save_redact(self):
        self.__add_button.click()

    def click_back(self):
        self.__back.click()

    def find_delete_button(self):
        return self.__delete_buttons_list.find_elements()

    def click_confirm_delete(self):
        self.__confirm_delete.click()