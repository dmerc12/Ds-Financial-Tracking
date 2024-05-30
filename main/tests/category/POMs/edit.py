from tests.category.POMs.create import create_deposit_category, create_expense_category
from selenium.webdriver.common.by import By

# POM for edit deposit category feature
def edit_deposit_category(self, title, username, password, name, new_name):
    create_deposit_category(self, 'Managing Deposits', username, password, name)
    self.driver.find_element(By.ID, 'category-update-btn').click()
    self.driver.find_element(By.NAME, 'name').clear()
    self.driver.find_element(By.NAME, 'name').send_keys(new_name)
    self.driver.find_element(By.ID, 'updateCategoryButton').click()
    self.assertEqual(self.driver.title, title)

# POM for edit expense category feature
def edit_expense_category(self, title, username, password, name, new_name):
    create_expense_category(self, 'Managing Expenses', username, password, name)
    self.driver.find_element(By.ID, 'category-update-btn').click()
    self.driver.find_element(By.NAME, 'name').clear()
    self.driver.find_element(By.NAME, 'name').send_keys(new_name)
    self.driver.find_element(By.ID, 'updateCategoryButton').click()
    self.assertEqual(self.driver.title, title)
