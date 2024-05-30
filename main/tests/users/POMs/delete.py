from selenium.webdriver.common.by import By
from tests.users.POMs.login import login

# POM for delete user feature
def delete_user(self, title, username, password):
    login(self, 'Home', username, password)
    self.driver.find_element(By.ID, 'manageInfoButton').click()
    self.driver.find_element(By.ID, 'deleteUserLink').click()
    self.driver.find_element(By.ID, 'deleteUserButton').click()
    self.assertEqual(self.driver.title, title)
