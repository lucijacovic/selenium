import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmationPage import ConfirmationPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        # Homepage
        homePage = HomePage(self.driver) # send driver to class
        # self.driver.find_element_by_css_selector("a[href*='shop']").click()

        # Checkout Page
        checkoutPage = homePage.shopItems()
        # products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        log.info("Getting all products")
        products = checkoutPage.getProducts()

        for product in products:
            # productName = product.find_element_by_xpath("div/h4/a").text  # //div[@class='card h-100']/div/h4/a
            productName = checkoutPage.getProductName(product).text
            log.info(productName)
            if productName == "Blackberry":
                # add item to card, //div[@class='card h-100']/div/button
                # product.find_element_by_xpath("div/button").click()
                checkoutPage.addProductToCart(product).click()

        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        checkoutPage.checkoutItems().click()
        # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

        # Confirmation Page
        confirmationPage = checkoutPage.checkoutItemsFinal()
        # confirmationPage = ConfirmationPage(self.driver)
        # self.driver.find_element_by_id("country").send_keys("cro")
        log.info("Entering country name as cro")
        confirmationPage.enterText().send_keys("cro")

        # wait = WebDriverWait(self.driver, 8)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Croatia")))  # duple zagrade za explicit wait uvik!
        self.verifyLinkPresence("Croatia")

        # self.driver.find_element_by_link_text("Croatia").click()
        confirmationPage.chooseCountry().click()
        # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        confirmationPage.markCheckbox().click()
        # self.driver.find_element_by_css_selector("[type='submit']").click()
        confirmationPage.purchaseItems().click()
        # success = self.driver.find_element_by_class_name("alert-success").text
        success = confirmationPage.successMessage().text
        log.info("Text received from app is" + success)

        assert "Success! Thank you!" in success
        # assert "Success! Thankdbhjssjab!" in success
