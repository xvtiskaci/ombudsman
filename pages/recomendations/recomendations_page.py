import time

from selenium.webdriver.common.by import By

from elements.button import Button
from pages.base_form import BaseForm


class RecommendationsPage(BaseForm):

    __add_recommendation_button = Button(By.XPATH, "//button[@class='_AppButton_16gsi_1 _AppButton--Green_16gsi_82']", "recommendation button")
    __rec_pages = Button(By.XPATH, "(//li[@class='_AppPagination__ListItem--Page_15ves_15'])", "peijebis raodenoba")
    __added_rec_list = Button(By.XPATH, "//div[@class='_AppRecommendationListing_9cl1q_1']//a", "damatebuli rekomendaciebi gverdze")

    def __init__(self):
        super().__init__(By.XPATH, "//h1[contains(text(),'ყველა რეკომენდაცია')]", "title")

    def add_recommendation(self):
        time.sleep(3)
        self.__add_recommendation_button.click()

    def get_rec_pages(self):
        return self.__rec_pages.find_elements()

    def get_added_rec(self):
        return self.__added_rec_list.find_elements()
