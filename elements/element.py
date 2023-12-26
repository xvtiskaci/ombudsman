from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from managers.DriverManager import DriverManager
from utils.LoggerUtils import LoggerUtils


class Element:

    def __init__(self, by=By.XPATH, locator=None, name=None):
        self.locator = locator
        self.name = name
        self.by = by

    def find_element(self):
        LoggerUtils.info("Finding element by Locator: {}".format(self.name))
        return DriverManager.get_driver().find_element(self.by, self.locator)

    def find_elements(self):
        LoggerUtils.info("find elements: {}".format(self.name))
        return DriverManager.get_driver().find_elements(self.by, self.locator)

    def is_visible(self):
        LoggerUtils.info("element is visible: {}".format(self.name))
        return DriverManager.get_driver().find_element(self.by, self.locator).is_displayed()

    def is_exists(self):
        LoggerUtils.info("element is exists: {}".format(self.name))
        if len(DriverManager.get_driver().find_elements(self.by, self.locator)) > 0:
            return True
        else:
            return False

    def click(self):
        LoggerUtils.info("clicking on element: {}".format(self.name))
        DriverManager.get_driver().find_element(self.by, self.locator).click()

    def get_text(self):
        LoggerUtils.info("get text from element: {}".format(self.name))
        return DriverManager.get_driver().find_element(self.by, self.locator).text

    def get_text_from_attribute(self, name):
        LoggerUtils.info("get text from element attribute: {}".format(self.name))
        return DriverManager.get_driver().find_element(self.by, self.locator).get_attribute(name)

    def is_enabled(self):
        LoggerUtils.info("element is enabled: {}".format(self.name))
        return DriverManager.get_driver().find_element(self.by, self.locator).is_enabled()

    def clear(self):
        LoggerUtils.info("clear element: {}".format(self.name))
        DriverManager.get_driver().find_element(self.by, self.locator).clear()


    def multiple_click(self, count):
        for i in range(count):
            self.click()


    def move_to_element(self):
        LoggerUtils.info("move to element: {}".format(self.name))
        ActionChains(DriverManager.get_driver()).move_to_element(self.find_element()).perform()







