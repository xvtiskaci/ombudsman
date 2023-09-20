from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from elements.element import Element
from managers.DriverManager import DriverManager
from utils.LoggerUtils import LoggerUtils


class Input(Element):
    def __init__(self, by, locator, name):
        super().__init__(by, locator, name)

    def send_text(self, value):
        LoggerUtils.info("sent text to element: {}".format(self.name))
        return DriverManager.get_driver().find_element(By.XPATH, self.locator).send_keys(value)

    def clear_and_fill(self, value):
        LoggerUtils.info("clear and fill element: {}".format(self.name))
        DriverManager.get_driver().find_element(By.XPATH, self.locator).clear()
        return self.send_text(value)

    def upload_image(self, path):
        return DriverManager.get_driver().find_element(By.XPATH, self.locator).send_keys(path)

    def press_enter(self):
        return DriverManager.get_driver().find_element(self.by, self.locator).send_keys(Keys.ENTER)
