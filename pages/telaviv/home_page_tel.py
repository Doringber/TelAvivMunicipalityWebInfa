from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locator import Locator
from tests.conftest import screen_shot


class HomePageTelAviv(BasePage):
    url = 'https://www.tel-aviv.gov.il/Pages/HomePage.aspx'

    @property
    def login_button(self):
        locator = Locator(By.XPATH, '//*[@id="ctl00_ctl51_ctl03_lnkDigitelLogin2"]')
        return BaseElement(
            driver=self.driver,
            locator=locator

        )

    @property
    def search_button(self):
        locator = Locator(By.XPATH, '//*[@id="ctl00_ctl51_ctl03_liSearch"]/a')
        return BaseElement(
            driver=self.driver,
            locator=locator

        )
