from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for update expense page
class UpdateExpensePOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking update expense button on update expense page
    def click_update_expense_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'updateExpenseButton')
        return element.click()
