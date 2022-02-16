from selenium.webdriver.common.by import By

# Checkout Page is actually Shop
from pageObjects.ConfirmationPage import ConfirmationPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    product = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "div/h4/a")
    addProduct = (By.XPATH, "div/button")
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout_final = (By.XPATH, "//button[@class='btn btn-success']")

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.product)

    def getProductName(self, product):
        return product.find_element(*CheckoutPage.productName)

    def addProductToCart(self, product):
        return product.find_element(*CheckoutPage.addProduct)

    def checkoutItems(self):
        return self.driver.find_element(*CheckoutPage.checkout)

    def checkoutItemsFinal(self):
        self.driver.find_element(*CheckoutPage.checkout_final).click()
        confirmationPage = ConfirmationPage(self.driver)
        return confirmationPage