from tests.category.POMs.create import create_deposit_category, create_expense_category
from selenium.webdriver.common.by import By

# POM for delete deposit category feature
def delete_deposit_category(self, title, username, password, name):
    create_deposit_category(self, 'Managing Deposits', username, password, name)
    self.driver.find_element(By.ID, 'category-delete-btn').click()
    self.driver.find_element(By.ID, 'deleteCategoryButton').click()
    self.assertEqual(self.driver.title, title)

# POM for delete expense category feature
def delete_expense_category(self, title, username, password, name):
    create_expense_category(self, 'Managing Expenses', username, password, name)
    self.driver.find_element(By.ID, 'category-delete-btn').click()
    self.driver.find_element(By.ID, 'deleteCategoryButton').click()
    self.assertEqual(self.driver.title, title)
