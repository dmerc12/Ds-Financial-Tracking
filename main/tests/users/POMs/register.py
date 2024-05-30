from selenium.webdriver.common.by import By

# POM for register feature
def register(self, title, username='', first_name='', last_name='', email='', phone_number='', password1='', password2=''):
    self.driver.get(self.live_server_url)
    self.driver.find_element(By.ID, 'registerLink').click()
    self.driver.find_element(By.NAME, 'username').send_keys(username)
    self.driver.find_element(By.NAME, 'first_name').send_keys(first_name)
    self.driver.find_element(By.NAME, 'last_name').send_keys(last_name)
    self.driver.find_element(By.NAME, 'email').send_keys(email)
    self.driver.find_element(By.NAME, 'phone_number').send_keys(phone_number)
    self.driver.find_element(By.NAME, 'password1').send_keys(password1)
    self.driver.find_element(By.NAME, 'password2').send_keys(password2)
    self.driver.find_element(By.ID, 'registerButton').click()
    self.assertEqual(self.driver.title, title)
