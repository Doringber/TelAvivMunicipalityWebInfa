import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import screen_shot


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find( )
        # self.find_elements()

    def find(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator=self.locator)
            )
            self.web_element = element
            return None
        except:
            screen_shot(drvr=self.driver)

    def find_elements(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(locator=self.locator)
        )
        self.web_element = elements
        return self.web_element

    def click(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator=self.locator)
            )
            element.click( )
            return None
        except:
            screen_shot(drvr=self.driver)

    def type_text(self, text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator=self.locator)
            )
            element.send_keys(text)
            return None
        except:
            screen_shot(drvr=self.driver)

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text
