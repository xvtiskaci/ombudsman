import time

from pages.description.word_code_page import WordCodePage
from pages.navigation_form import NavigationForm
from steps.add_word_code_steps import AddWordCodePageSteps
from steps.login_page_steps import LoginPageSteps
from steps.word_code_page_steps import WordCodePageSteps


class TestWordCodes:
    def test_word_codes(self):
        login_steps = LoginPageSteps
        login_steps.login()
        word_code_page = WordCodePageSteps()
        word_code_page.go_to_word_code_page()
        add_word_code = AddWordCodePageSteps()
        add_word_code.add_word_code()
        time.sleep(5)