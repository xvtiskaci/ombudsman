import time

import pyautogui

from pages.recomendations.add_recommendation_page import AddRecommendationPage
from pages.recomendations.recomendations_page import RecommendationsPage
from steps.login_page_steps import LoginPageSteps


class TestRecommendations:

    def test_recommendation_should_be_added(self):
        login_steps = LoginPageSteps
        login_steps.login()
        recommendations_page = RecommendationsPage()
        recommendations_page.add_recommendation()
        add_rec_page = AddRecommendationPage()
        assert add_rec_page.is_visible()
        time.sleep(4)
        add_rec_page.fill_rec_txt(value="ragaca")
        add_rec_page.select_type()
        add_rec_page.click_recommendation()
        add_rec_page.check_year()
        add_rec_page.click_year()
        add_rec_page.click_date_picker()
        add_rec_page.click_pick_date()
        add_rec_page.click_establishment()
        add_rec_page.pick_parlament()
        add_rec_page.click_parliament_head()
        add_rec_page.click_life_rights()
        add_rec_page.click_word_code_bar()
        add_rec_page.click_word_wero()
        add_rec_page.fill_indicator_title(value="შესრულების ინდიკატორის სათაური")
        add_rec_page.add_activity(activiti="დამატებული აქტივობა ინდიკატორში")
        add_rec_page.click_add_activity_button()
        add_rec_page.fill_activity_child(value="აქტივობის შვილი")
        add_rec_page.click_plus_button()
        add_rec_page.fill_enother_indicator(value="სხვა ინდიკატორი")
        add_rec_page.fill_another_activiti(value="სხვა აქტივობა")
        add_rec_page.send_pdf()
        time.sleep(1)
        mypdf_path = r"C:\Users\ghvti\OneDrive\Desktop\rame.pdf"
        pyautogui.write(mypdf_path)
        pyautogui.press("enter")
        add_rec_page.click_add_button()
        time.sleep(3)

