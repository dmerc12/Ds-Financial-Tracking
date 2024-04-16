from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# POM for create expense page
class CreateExpensePOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    ## POM for selecting category on the expense form
    def select_category(self, category):
        element: WebElement = self.driver.find_element(By.ID, 'category')
        select = Select(element)
        select.select_by_visible_text(category)
        return select.first_selected_option.text

    ## POM for entering date on the expense form
    def enter_date(self, date):
        element: WebElement = self.driver.find_element(By.ID, 'date')
        return element.send_keys(date)

    ## POM for entering description on the expense form
    def enter_description(self, description):
        element: WebElement = self.driver.find_element(By.ID, 'description')
        return element.send_keys(description)

    ## POM for entering amount on the expense form
    def enter_amount(self, amount):
        element: WebElement = self.driver.find_element(By.ID, 'amount')
        return element.send_keys(amount)


    ## POM for clicking create expense button on create expense page
    def click_create_expense_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'createExpenseButton')
        return element.click()
