from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# POM for create deposit page
class CreateDepositPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for selecting category on the deposit form
    def select_category(self, category):
        element: WebElement = self.driver.find_element(By.ID, 'category')
        select = Select(element)
        select.select_by_visible_text(category)
        return select.first_selected_option.text

    ## POM for entering date on the deposit form
    def enter_date(self, date):
        element: WebElement = self.driver.find_element(By.ID, 'date')
        return element.send_keys(date)

    ## POM for entering description on the deposit form
    def enter_description(self, description):
        element: WebElement = self.driver.find_element(By.ID, 'description')
        return element.send_keys(description)

    ## POM for entering amount on the deposit form
    def enter_amount(self, amount):
        element: WebElement = self.driver.find_element(By.ID, 'amount')
        return element.send_keys(amount)


    ## POM for clicking create deposit button on create deposit page
    def click_create_deposit_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'createDepositButton')
        return element.click()

    ## POM for clicking back button on create deposit page
    def click_back_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'backButton')
        return element.click()
