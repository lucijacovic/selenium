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

        # Checkout Page
        checkoutPage = homePage.shopItems()
        log.info("Getting all products")
        products = checkoutPage.getProducts()

        for product in products:
            productName = checkoutPage.getProductName(product).text
            log.info(productName)
            if productName == "Blackberry":
                checkoutPage.addProductToCart(product).click()

        checkoutPage.checkoutItems().click()

        # Confirmation Page
        confirmationPage = checkoutPage.checkoutItemsFinal()
        log.info("Entering country name as cro")
        confirmationPage.enterText().send_keys("cro")

        self.verifyLinkPresence("Croatia")

        confirmationPage.chooseCountry().click()
        confirmationPage.markCheckbox().click()
        confirmationPage.purchaseItems().click()
        success = confirmationPage.successMessage().text
        log.info("Text received from app is" + success)

        assert "Success! Thank you!" in success
