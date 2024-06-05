from tests.expense.POMs.create import create_expense
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# POM for edit expense feature
def edit_expense(self, title, username, password, category_name, category_index, date, description, amount, expense_id, new_category_index, new_date, new_description, new_amount):
    create_expense(self, 'Managing Expenses', username, password, category_name, category_index, date, description, amount)
    self.driver.find_element(By.ID, f'expense-{expense_id}').click()
    self.driver.find_element(By.ID, 'updateExpenseLink').click()
    category_dropdown = self.driver.find_element(By.NAME, 'category')
    category_select = Select(category_dropdown)
    category_select.select_by_index(new_category_index)
    self.driver.find_element(By.NAME, 'date').clear()
    self.driver.find_element(By.NAME, 'date').send_keys(new_date)
    self.driver.find_element(By.NAME, 'description').clear()
    self.driver.find_element(By.NAME, 'description').send_keys(new_description)
    self.driver.find_element(By.NAME, 'amount').clear()
    self.driver.find_element(By.NAME, 'amount').send_keys(new_amount)
    self.driver.find_element(By.ID, 'updateExpenseButton').click()
    self.assertEqual(self.driver.title, title)
