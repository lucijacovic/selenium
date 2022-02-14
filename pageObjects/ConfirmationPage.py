from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_id("country").send_keys("cro")
    inputText = (By.ID, "country")
    # self.driver.find_element_by_link_text("Croatia").click()
    country = (By.LINK_TEXT, "Croatia")
    # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # self.driver.find_element_by_css_selector("[type='submit']").click() # Purchase button
    purchase = (By.CSS_SELECTOR, "[type='submit']")
    # success = self.driver.find_element_by_class_name("alert-success").text
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