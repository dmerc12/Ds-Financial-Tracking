from selenium.webdriver.common.by import By
from tests.users.POMs.login import login

# POM for change password feature
def change_password(self, title, username, password, new_password1, new_password2):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'manageInfoButton').click()
    self.driver.find_element(By.ID, 'changePasswordLink').click()
    self.driver.find_element(By.NAME, 'new_password1').send_keys(new_password1)
    self.driver.find_element(By.NAME, 'new_password2').send_keys(new_password2)
    self.driver.find_element(By.ID, 'changePasswordButton').click()
    self.assertEqual(self.driver.title, title)
