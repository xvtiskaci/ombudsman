import time

from pages.description.word_code_page import WordCodePage
from pages.navigation_form import NavigationForm


class WordCodePageSteps:

    @staticmethod
    def go_to_word_code_page():
        word_code_page = WordCodePage()
        nav_form = NavigationForm()
        assert nav_form.is_visible()
        nav_form.click_description_button()
        word_code_page.click_word_codes_button()
        assert word_code_page.is_visible()
        word_code_page.click_new_word_code_button()