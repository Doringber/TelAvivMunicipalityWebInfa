from pytest import fixture
import datetime
import inspect
import logging
import os
import time
from os import path
from shutil import rmtree

from selenium import webdriver

from tests.config import Config


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests against"
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


@fixture(scope='session')
def test_logger():
    import os
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    logfile = os.path.join(os.path.dirname(os.path.relpath(__file__)), "test_log.log")
    handler = logging.FileHandler(logfile)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)


@fixture(params=[webdriver.Chrome])
def browser(request):
    global driver
    driver = request.param
    drvr = driver( )
    logger_test( )

    yield drvr
    drvr.quit( )


def logger_test(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called

    '''
    Public Implementation
    '''

    loggerName = inspect.stack( )[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    # Create logs path if not exits
    if not path.exists('logs'):
        os.makedirs('logs')

    # Remove test folder if already exits
    if path.exists('logs'):
        rmtree('logs')
    os.makedirs('logs')

    fileHandler = logging.FileHandler(
        "/Users/doringber/PycharmProjects/frameworks/ImdbAutomationinfrastucture/logs/Automation_{}.log".format(
            loggerName), mode='w')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger


def screen_shot(drvr=None):
    fileName = datetime.datetime.now( ).strftime("%Y%m%dT%H:%M:%S") + ".png"
    screenshotDirectory = "../screenshots/"
    relativeFileName = screenshotDirectory + fileName
    currentDirectory = os.path.dirname(__file__)
    destinationFile = os.path.join(currentDirectory, relativeFileName)
    destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

    try:
        if not os.path.exists(destinationDirectory):
            os.makedirs(destinationDirectory)

        time.sleep(2)
        drvr.get_screenshot_as_file(destinationFile)
        # log.info("Screenshot save to directory: " + destinationFile)
    except:
        print('Screen shot have problems...')
        # self.log.error("### Exception Occurred when taking screenshot")
