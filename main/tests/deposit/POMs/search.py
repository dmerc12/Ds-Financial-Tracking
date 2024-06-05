from tests.deposit.POMs.create import create_deposit
from selenium.webdriver.common.by import By

# POM for deposit search feature
def deposit_search(self, title, username, password, category_name, category_index, date, description, amount, deposit_id, start_date, end_date):
    create_deposit(self, 'Managing Deposits', username, password, category_name, category_index, date, description, amount)
    self.driver.find_element(By.ID, 'search-toggle').click()
    self.driver.find_element(By.NAME, 'deposit_id').send_keys(deposit_id)
    self.driver.find_element(By.NAME, 'start_date').send_keys(start_date)
    self.driver.find_element(By.NAME, 'end_date').send_keys(end_date)
    self.driver.find_element(By.ID, 'searchButton').click()
    self.assertEqual(self.driver.title, title)
