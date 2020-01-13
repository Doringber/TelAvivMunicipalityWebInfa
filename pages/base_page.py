import logging
import time


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def window_handles(self,number):
        return self.driver.window_handles[number]

    def switch_to(self,window,wait):
        time.sleep(wait)
        self.driver.switch_to.window(window_name=window)



