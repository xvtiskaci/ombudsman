import time

from selenium.webdriver.common.by import By

from elements.button import Button
from pages.base_form import BaseForm


class RecommendationsPage(BaseForm):

    __add_recommendation_button = Button(By.XPATH, "//button[@class='_AppButton_16gsi_1 _AppButton--Green_16gsi_82']", "recommendation button")

    def __init__(self):
        super().__init__(By.XPATH, "//h1[contains(text(),'ყველა რეკომენდაცია')]", "title")

    def add_recommendation(self):
        time.sleep(3)
        self.__add_recommendation_button.click()
