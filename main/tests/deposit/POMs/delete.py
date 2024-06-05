from tests.deposit.POMs.create import create_deposit
from selenium.webdriver.common.by import By

# POM for delete deposit feature
def delete_deposit(self, title, username, password, category_name, category_index, date, description, amount, deposit_id):
    create_deposit(self, 'Managing Deposits', username, password, category_name, category_index, date, description, amount)
    self.driver.find_element(By.ID, f'deposit-{deposit_id}').click()
    self.driver.find_element(By.ID, 'deleteDepositLink').click()
    self.driver.find_element(By.ID, 'deleteDepositButton').click()
    self.assertEqual(self.driver.title, title)
