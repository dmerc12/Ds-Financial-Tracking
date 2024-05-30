from selenium.webdriver.common.by import By
from tests.users.POMs.login import login

# POM for edit user feature
def edit_user(self, title, username='', password='', new_username='', new_first_name='', new_last_name='', new_email='', new_phone_number=''):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'manageInfoButton').click()
    username = self.driver.find_element(By.NAME, 'username')
    username.clear()
    username.send_keys(new_username)
    first_name = self.driver.find_element(By.NAME, 'first_name')
    first_name.clear()
    first_name.send_keys(new_first_name)
    last_name = self.driver.find_element(By.NAME, 'last_name')
    last_name.clear()
    last_name.send_keys(new_last_name)
    email = self.driver.find_element(By.NAME, 'email')
    email.clear()
    email.send_keys(new_email)
    phone_number = self.driver.find_element(By.NAME, 'phone_number')
    phone_number.clear()
    phone_number.send_keys(new_phone_number)
    self.driver.find_element(By.ID, 'updateUserButton').click()
    self.assertEqual(self.driver.title, title)
