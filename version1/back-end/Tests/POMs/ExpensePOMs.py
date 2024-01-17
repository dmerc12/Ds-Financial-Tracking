from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.safari.webdriver import WebDriver
# from selenium.webdriver.edge.webdriver import WebDriver

class ExpensePOMs:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_manage_expenses_nav_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageExpensesNavButton")
        return element.click()

    def click_manage_expenses_button(self):
        element: WebElement = self.driver.find_element(By.ID, "manageExpensesButton")
        return element.click()

    def click_create_expense_modal(self):
        element: WebElement = self.driver.find_element(By.ID, "createExpenseModal")
        return element.click()

    def select_create_expense_category_id(self, category_id):
        element: WebElement = self.driver.find_element(By.ID, "createExpenseCategoryInput")
        return element.send_keys(category_id)

    def input_create_expense_date(self, date):
        element: WebElement = self.driver.find_element(By.ID, "createExpenseDateInput")
        return element.send_keys(date)

    def input_create_expense_description(self, description):
        element: WebElement = self.driver.find_element(By.ID, "createExpenseDescriptionInput")
        return element.send_keys(description)

    def input_create_expense_amount(self, amount):
        element: WebElement = self.driver.find_element(By.ID, "createExpenseAmountInput")
        return element.send_keys(amount)

    def click_create_expense_button(self):
        element: WebElement = self.driver.find_element(By.ID, "createExpenseButton")
        return element.click()

    def click_update_expense_modal(self, expense_id):
        element: WebElement = self.driver.find_element(By.ID, f"updateExpenseModal{expense_id}")
        return element.click()

    def select_update_expense_category_id(self, category_id):
        element: WebElement = self.driver.find_element(By.ID, "updateExpenseCategoryInput")
        return element.send_keys(category_id)

    def input_update_expense_date(self, date):
        element: WebElement = self.driver.find_element(By.ID, "updateExpenseDateInput")
        return element.send_keys(date)

    def input_update_expense_description(self, description):
        element: WebElement = self.driver.find_element(By.ID, "updateExpenseDescriptionInput")
        return element.send_keys(description)

    def input_update_expense_amount(self, amount):
        element: WebElement = self.driver.find_element(By.ID, "updateExpenseAmountInput")
        return element.send_keys(amount)

    def click_update_expense_button(self):
        element: WebElement = self.driver.find_element(By.ID, "updateExpenseButton")
        return element.click()

    def click_delete_expense_modal(self, expense_id):
        element: WebElement = self.driver.find_element(By.ID, f"deleteExpenseModal{expense_id}")
        return element.click()

    def click_delete_expense_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deleteExpenseButton")
        return element.click()
