from selenium.webdriver.common.by import By

# Checkout Page is actually Shop
from pageObjects.ConfirmationPage import ConfirmationPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # find_elements_by_xpath("//div[@class='card h-100']")
    product = (By.XPATH, "//div[@class='card h-100']")
    # productName = product.find_element_by_xpath("div/h4/a").text
    productName = (By.XPATH, "div/h4/a")
    # add item to card, //div[@class='card h-100']/div/button
    # product.find_element_by_xpath("div/button").click()
    addProduct = (By.XPATH, "div/button")
    # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
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