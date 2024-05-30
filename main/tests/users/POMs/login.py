from selenium.webdriver.common.by import By

# POM for login feature
def login(self, title, username='', password=''):
    self.driver.get(self.live_server_url)
    self.driver.find_element(By.NAME, 'username').send_keys(username)
    self.driver.find_element(By.NAME, 'password').send_keys(password)
    self.driver.find_element(By.ID, 'loginButton').click()
    self.assertEqual(self.driver.title, title)
