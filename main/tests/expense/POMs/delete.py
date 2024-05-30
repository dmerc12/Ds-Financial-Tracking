from tests.expense.POMs.create import create_expense
from selenium.webdriver.common.by import By

# POM for delete expense feature
def delete_expense(self, title, username, password, category_name, category_index, date, description, amount, expense_id):
    create_expense(self, 'Managing Expenses', username, password, category_name, category_index, date, description, amount)
    self.driver.find_element(By.ID, f'expense-{expense_id}').click()
    self.driver.find_element(By.ID, 'deleteExpenseLink').click()
    self.driver.find_element(By.ID, 'deleteExpenseButton').click()
    self.assertEqual(self.driver.title, title)
