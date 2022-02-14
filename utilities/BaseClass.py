import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")

class BaseClass:
    #def __init__(self, driver):
    #    self.driver = driver
    # not needed, driver defined in conftest.py

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 8).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Croatia")))  # duple zagrade za explicit wait uvik!

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
        # dropdown = Select(homePage.getGender())
        # dropdown.select_by_visible_text("Female")

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        # fileHandler = logging.FileHandler('C:\Users\lucij\PycharmProjects1\PythonSelFramework\utilities\logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        if (logger.hasHandlers()): # clear double logs
            logger.handlers.clear()
        logger.addHandler(fileHandler)  # fileHandler object (file location)
        logger.setLevel(logging.DEBUG)
        return logger