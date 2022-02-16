from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    inputText = (By.ID, "country")
    country = (By.LINK_TEXT, "Croatia")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "[type='submit']")
    success = (By.CLASS_NAME, "alert-success")

    def enterText(self):
        return self.driver.find_element(*ConfirmationPage.inputText)

    def chooseCountry(self):
        return self.driver.find_element(*ConfirmationPage.country)

    def markCheckbox(self):
        return self.driver.find_element(*ConfirmationPage.checkbox)

    def purchaseItems(self):
        return self.driver.find_element(*ConfirmationPage.purchase)

    def successMessage(self):
        return self.driver.find_element(*ConfirmationPage.success)