from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By

# POM for delete expense page
class DeleteExpensePOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for clicking delete expense button on delete expense page
    def click_delete_expense_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'deleteExpenseButton')
        return element.click()
