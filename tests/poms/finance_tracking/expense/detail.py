from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for expense detail page
class ExpenseDetailPOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking update expense button on expense detail page
    def click_update_expense_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'updateExpenseLink')
        return element.click()

    ## POM for clicking delete expense button on expense detail page
    def click_delete_expense_link(self):
        element: WebElement = self.driver.find_element(By.ID, 'deleteExpenseLink')
        return element.click()
