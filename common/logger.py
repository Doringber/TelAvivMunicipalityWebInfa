
import logging
import datetime
from os import path
from json import loads
from os import makedirs
from shutil import rmtree
from termcolor import colored
import selenium.webdriver as webdriver


'''
Defines
'''
LOG_TEST_FAILED_WITH_ERROR = "Test '%s' failed with error message: '%s'"


class Logger(object):
    __instance = None

    '''
    Public Implementation
    '''
    @staticmethod
    def get_instance():
        """ Static access method. """
        if Logger.__instance is None:
            Logger()

        return Logger.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Logger.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Logger.__instance = self

    def initialization(self, test):
        self.logger = None
        self.test_logs_path = None
        # self.driver = None
        self.browser = None
        self.test_name = None
        self.counter = 0
        self.test = test
        self.test_name = test.id().split(".")[-1]
        # self.platform_type = Configuration.get_instance().platform_type()
        self.__setup_logger__()

    def warning(self, class_ptr, method, message):
        message = class_ptr.__class__.__name__ + " : " + method + " : " + message
        self.logger.warning(message)

    def error(self, class_ptr, method, message):
        message = class_ptr.__class__.__name__ + " : " + method + " : " + message
        print(colored("Error: %s" % message, "red"))
        self.logger.error(message)

    def info(self, class_ptr, method, message):
        message = class_ptr.__class__.__name__ + " : " + method + " : " + message
        self.logger.info(message)

    def take_screenshot(self):
        # assert description is None or isinstance(description, str)

        # if self.driver is not None and self.driver.driver is not None:
        # description = "_"+description if description is not None else ""
        # screenshot_file_path = self.test_logs_path + "/" + str(self.counter) + description + "_screenshot.png"
        # TestBase(self).take_screenshot()

        self.counter += 1

    def log_assert(self, condition, message, with_snapshot=True):
        if not condition:
            # if with_snapshot:
                # self.take_screenshot()
            self.error("None", "None", message)

            print(colored(LOG_TEST_FAILED_WITH_ERROR % (self.test_name, message), "red"))
            assert 0

    def get_current_time(self, format):
        return datetime.datetime.now().strftime(format)

    def close_logs(self):
        if self.logger.handlers:
            for handler in self.logger.handlers:
                handler.close()

        if self.driver is not None and self.driver.driver is not None:
            self.__write_log_from_type__("device")

            # if Configuration.get_instance().is_selenium_based_test():
            log_file = open(self.test_logs_path + "/dom.html", 'w')
            log_file.write(self.driver.get_dom_tree())
            log_file.close()

    def set_appium_driver(self, driver):
        self.driver = driver

    def get_device_log(self):
        return self.driver.get_device_log()


    '''
    Private Implementation
    '''
    def __write_log_from_type__(self, file_name):
        log = self.driver.get_device_log()

        log_file = open(self.test_logs_path + "/" + file_name + ".log", 'w')
        for line in log:
            log_line = ''
            for attribute in line:
                log_line += str(line[attribute]) + ' '

            log_file.write(log_line + '\n')
        log_file.close()

    def __setup_logger__(self):

        # Setup logs folder path
        self.test_logs_path = 'logs/' + self.test_name

        # Create logs path if not exits
        if not path.exists('logs'):
            makedirs('logs')

        # Remove test folder if already exits
        if path.exists(self.test_logs_path):
            rmtree(self.test_logs_path)
        makedirs(self.test_logs_path)

        # create logger
        self.logger = logging.getLogger('AutomationLogger')
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(self.test_logs_path + "/" + "test.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s : %(levelname)s : %(message)s'))
        self.logger.addHandler(file_handler)
