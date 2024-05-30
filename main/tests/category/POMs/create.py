from selenium.webdriver.common.by import By
from tests.users.POMs.login import login

# POM for create deposit category feature
def create_deposit_category(self, title, username, password, name):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesButton').click()
    self.driver.find_element(By.ID, 'depositHomeLink').click()
    self.driver.find_element(By.ID, 'createCategoryLink').click()
    self.driver.find_element(By.NAME, 'name').send_keys(name)
    self.driver.find_element(By.ID, 'createCategoryButton').click()
    self.assertEqual(self.driver.title, title)

# POM for create expense category feature
def create_expense_category(self, title, username, password, name):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'trackFinancesButton').click()
    self.driver.find_element(By.ID, 'expenseHomeLink').click()
    self.driver.find_element(By.ID, 'createCategoryLink').click()
    self.driver.find_element(By.NAME, 'name').send_keys(name)
    self.driver.find_element(By.ID, 'createCategoryButton').click()
    self.assertEqual(self.driver.title, title)
