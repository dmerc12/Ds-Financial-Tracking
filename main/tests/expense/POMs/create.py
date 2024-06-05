from tests.category.POMs.create import create_expense_category
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# POM for create expense feature
def create_expense(self, title, username, password, category_name, category_index, date, description, amount):
    create_expense_category(self, 'Managing Expenses', username, password, category_name)
    self.driver.find_element(By.ID, 'createExpenseLink').click()
    category_dropdown = self.driver.find_element(By.NAME, 'category')
    category_select = Select(category_dropdown)
    category_select.select_by_index(category_index)
    self.driver.find_element(By.NAME, 'date').send_keys(date)
    self.driver.find_element(By.NAME, 'description').send_keys(description)
    self.driver.find_element(By.NAME, 'amount').send_keys(amount)
    self.driver.find_element(By.ID, 'createExpenseButton').click()
    self.assertEqual(self.driver.title, title)
