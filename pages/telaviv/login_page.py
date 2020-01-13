from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locator import Locator


class LoginTelAviv(BasePage):
    url = 'https://ssop.tel-aviv.gov.il/adfs/ls/?wa=wsignin1.0&wtrealm=urn%3asharepoint%3aintranet&wctx=http%3a%2f%2fmydigitel.tel-aviv.gov.il%2f_layouts%2f15%2fAuthenticate.aspx%3fSource%3d%252F&whr=https://ssop.tel-aviv.gov.il/adfs/services/trust'

    @property
    def id(self):
        locator = Locator(By.ID, 'userNameInput')
        return BaseElement(
            driver=self.driver,
            locator=locator

        )

    @property
    def password(self):
        locator = Locator(By.ID, 'passwordInput')
        return BaseElement(
            driver=self.driver,
            locator=locator

        )

    @property
    def enter_button(self):
        locator = Locator(By.ID, 'submitButton')
        return BaseElement(
            driver=self.driver,
            locator=locator

        )

    @property
    def error_text(self):
        locator = Locator(By.ID, 'errorText')
        return BaseElement(
            driver=self.driver,
            locator=locator

        )
