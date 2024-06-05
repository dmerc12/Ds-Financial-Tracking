from tests.expense.POMs.create import create_expense
from selenium.webdriver.common.by import By

# POM for expense search feature
def expense_search(self, title, username, password, category_name, category_index, date, description, amount, expense_id, start_date, end_date):
    create_expense(self, 'Managing Expenses', username, password, category_name, category_index, date, description, amount)
    self.driver.find_element(By.ID, 'search-toggle').click()
    self.driver.find_element(By.NAME, 'expense_id').send_keys(expense_id)
    self.driver.find_element(By.NAME, 'start_date').send_keys(start_date)
    self.driver.find_element(By.NAME, 'end_date').send_keys(end_date)
    self.driver.find_element(By.ID, 'searchButton').click()
    self.assertEqual(self.driver.title, title)
