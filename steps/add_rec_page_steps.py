from datetime import time

import pyautogui

from pages.recomendations.add_recommendation_page import AddRecommendationPage


class AddRecPageSteps:
    @staticmethod
    def fill_rec_form():
        add_recommendation_page = AddRecommendationPage()
        assert add_recommendation_page.is_visible()
        add_recommendation_page.fill_rec_txt(value="ragaca")
        add_recommendation_page.select_type()
        add_recommendation_page.click_recommendation()
        add_recommendation_page.check_year()
        add_recommendation_page.click_year()
        add_recommendation_page.click_date_picker()
        add_recommendation_page.click_pick_date()
        add_recommendation_page.click_establishment()
        add_recommendation_page.pick_parlament()
        add_recommendation_page.click_parliament_head()
        add_recommendation_page.click_life_rights()
        add_recommendation_page.click_word_code_bar()
        add_recommendation_page.click_word_wero()
        add_recommendation_page.fill_indicator_title(value="შესრულების ინდიკატორის სათაური")
        add_recommendation_page.add_activity(activiti="დამატებული აქტივობა ინდიკატორში")
        add_recommendation_page.click_add_activity_button()
        add_recommendation_page.fill_activity_child(value="აქტივობის შვილი")
        add_recommendation_page.click_plus_button()
        add_recommendation_page.fill_enother_indicator(value="სხვა ინდიკატორი")
        add_recommendation_page.fill_another_activiti(value="სხვა აქტივობა")
        add_recommendation_page.send_pdf()
        mypdf_path = r"C:\Users\artme\OneDrive\Desktop\rame.pdf"
        pyautogui.write(mypdf_path)
        pyautogui.press("enter")
        add_recommendation_page.click_add_button()