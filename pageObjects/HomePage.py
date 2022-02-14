from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']") # self.driver.find_element_by_css_selector("input[name='name']").send_keys("Lucija")
    email = (By.NAME, "email") # self.driver.find_element_by_name("email").send_keys("mail@examaple.com")
    checkbox = (By.ID, "exampleCheck1") # self.driver.find_element_by_id("exampleCheck1").click()
    gender = (By.ID, "exampleFormControlSelect1") # (self.driver.find_element_by_id("exampleFormControlSelect1"))
    submit = (By.XPATH, "//input[@type='submit']") # self.driver.find_element_by_xpath("//input[@type='submit']").click()
    message = (By.CLASS_NAME, "alert-success") # message = self.driver.find_element_by_class_name("alert-success").text
    def shopItems(self): # method for clicking the shop button, leads to
        # self.driver.find_element_by_css_selector("a[href*='shop']")
        # find trigger that navigates to next page eg. button
        self.driver.find_element(*HomePage.shop).click() # * will iterate and print all element
        checkoutPage = CheckoutPage(self.driver) # Shop page
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.message)