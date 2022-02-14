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
        homePage.getName().send_keys(getData["firstname"]) # homePage.getName().send_keys("Lucija")
        homePage.getEmail().send_keys(getData["email"]) # homePage.getEmail().send_keys("mail@examaple.com")
        homePage.getCheckbox().click()

        self.selectOptionByText(homePage.getGender(), getData["gender"]) # self.selectOptionByText(homePage.getGender(), "Female")
        # dropdown = Select(homePage.getGender())
        # dropdown.select_by_visible_text("Female")

        homePage.submitForm().click()

        message = homePage.getSuccessMessage().text
        assert "success" in message
        self.driver.refresh() # multiple dataset on same page


    @pytest.fixture(params= HomePageData.test_HomePage_data) # @pytest.fixture(params=(("Lucija", "mail@examaple.com", "Female"), ("Jens", "mail2@examaple.com", "Male")))
    # @pytest.fixture(params=HomePageData.getTestData("Testcase2")) # excel
    def getData(self, request):
        return request.param
