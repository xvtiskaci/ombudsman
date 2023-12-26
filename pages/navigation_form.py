from selenium.webdriver.common.by import By

from elements.button import Button
from pages.base_form import BaseForm


class NavigationForm(BaseForm):
    __description_button = Button(By.XPATH, "//span[contains(text(),'დახარისხება')]", "daxasiatebebi")

    def __init__(self):
        super().__init__(By.XPATH, "//div[@class='_AppSideBar__Content_2b3f6_15']", "unique")

    def click_description_button(self):
        self.__description_button.click()
