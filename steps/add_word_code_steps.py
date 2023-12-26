import time

from faker import Faker

from pages.description.add_word_codes_page import AddWordCodePage
from pages.description.word_code_page import WordCodePage


class AddWordCodePageSteps:

    @staticmethod
    def add_word_code():
        fake = Faker()
        word_code_txt = fake.word()
        red_word_code_txt = fake.word()
        add_word_code_page = AddWordCodePage()
        assert add_word_code_page.is_visible()
        add_word_code_page.fill_word_code_name(word_code_txt)
        add_word_code_page.click_add_word_code_name_button()
        wr = WordCodePage()
        assert wr.is_visible()
        # word_code_list = wr.get_last_word_code()
        # last_word = word_code_list[len(word_code_list) - 1]
        # last_word.click()
        # assert add_word_code_page.is_visible()
        # add_word_code_page.redact_fill_word_code_name(red_word_code_txt)
        # add_word_code_page.click_add_word_code_name_button()
        # assert wr.is_visible()
        # word_code_for_delate = wr.get_last_word_for_delete()
        # last_word_delate = word_code_for_delate[len(word_code_for_delate) - 1]
        # last_word_delate.click()
        # wr.del_button_click()
