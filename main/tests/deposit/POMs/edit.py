from tests.deposit.POMs.create import create_deposit
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# POM for edit deposit feature
def edit_deposit(self, title, username, password, category_name, category_index, date, description, amount, deposit_id, new_category_index, new_date, new_description, new_amount):
    create_deposit(self, 'Managing Deposits', username, password, category_name, category_index, date, description, amount)
    self.driver.find_element(By.ID, f'deposit-{deposit_id}').click()
    self.driver.find_element(By.ID, 'updateDepositLink').click()
    category_dropdown = self.driver.find_element(By.NAME, 'category')
    category_select = Select(category_dropdown)
    category_select.select_by_index(new_category_index)
    self.driver.find_element(By.NAME, 'date').clear()
    self.driver.find_element(By.NAME, 'date').send_keys(new_date)
    self.driver.find_element(By.NAME, 'description').clear()
    self.driver.find_element(By.NAME, 'description').send_keys(new_description)
    self.driver.find_element(By.NAME, 'amount').clear()
    self.driver.find_element(By.NAME, 'amount').send_keys(new_amount)
    self.driver.find_element(By.ID, 'updateDepositButton').click()
    self.assertEqual(self.driver.title, title)
