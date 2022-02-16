import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from testData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_FormSubmission(self, getData):
        log = self.getLogger()

        homePage = HomePage(self.driver)
        log.info("First name is " + getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getCheckbox().click()

        self.selectOptionByText(homePage.getGender(), getData["gender"])

        homePage.submitForm().click()

        message = homePage.getSuccessMessage().text
        assert "success" in message
        self.driver.refresh() # multiple dataset on same page


    @pytest.fixture(params= HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
