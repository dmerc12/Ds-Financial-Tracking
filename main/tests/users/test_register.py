from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase

# Tests for register feature
class RegisterTests(LiveServerTestCase):

    def setUp(self):
        self.driver = WebDriver()

    def tearDown(self):
        self.driver.close()

    ## Test register feature with empty username
    def test_register_feature_empty_username(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'registerLink').click()
        self.driver.find_element(By.NAME, 'username').send_keys('')
        self.driver.find_element(By.NAME, 'first_name').send_keys('first')
        self.driver.find_element(By.NAME, 'last_name').send_keys('last')
        self.driver.find_element(By.NAME, 'email').send_keys('test@email.com')
        self.driver.find_element(By.NAME, 'phone_number').send_keys('1-222-333-4444')
        self.driver.find_element(By.NAME, 'password1').send_keys('pass12345')
        self.driver.find_element(By.NAME, 'password2').send_keys('pass12345')
        self.driver.find_element(By.ID, 'registerButton').click()
        self.assertEqual(self.driver.title, 'Registering')

    ## Test register feature with empty first name
    def test_register_feature_empty_first_name(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'registerLink').click()
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'first_name').send_keys('')
        self.driver.find_element(By.NAME, 'last_name').send_keys('last')
        self.driver.find_element(By.NAME, 'email').send_keys('test@email.com')
        self.driver.find_element(By.NAME, 'phone_number').send_keys('1-222-333-4444')
        self.driver.find_element(By.NAME, 'password1').send_keys('pass12345')
        self.driver.find_element(By.NAME, 'password2').send_keys('pass12345')
        self.driver.find_element(By.ID, 'registerButton').click()
        self.assertEqual(self.driver.title, 'Registering')

    ## Test register feature with empty last name
    def test_register_feature_empty_last_name(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'registerLink').click()
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'first_name').send_keys('first')
        self.driver.find_element(By.NAME, 'last_name').send_keys('')
        self.driver.find_element(By.NAME, 'email').send_keys('test@email.com')
        self.driver.find_element(By.NAME, 'phone_number').send_keys('1-222-333-4444')
        self.driver.find_element(By.NAME, 'password1').send_keys('pass12345')
        self.driver.find_element(By.NAME, 'password2').send_keys('pass12345')
        self.driver.find_element(By.ID, 'registerButton').click()
        self.assertEqual(self.driver.title, 'Registering')

    ## Test register feature with empty email
    def test_register_feature_empty_email(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'registerLink').click()
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'first_name').send_keys('first')
        self.driver.find_element(By.NAME, 'last_name').send_keys('last')
        self.driver.find_element(By.NAME, 'email').send_keys('')
        self.driver.find_element(By.NAME, 'phone_number').send_keys('1-222-333-4444')
        self.driver.find_element(By.NAME, 'password1').send_keys('pass12345')
        self.driver.find_element(By.NAME, 'password2').send_keys('pass12345')
        self.driver.find_element(By.ID, 'registerButton').click()
        self.assertEqual(self.driver.title, 'Registering')

    ## Test register feature with empty phone number
    def test_register_feature_empty_phone_number(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'registerLink').click()
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'first_name').send_keys('first')
        self.driver.find_element(By.NAME, 'last_name').send_keys('last')
        self.driver.find_element(By.NAME, 'email').send_keys('test@email.com')
        self.driver.find_element(By.NAME, 'phone_number').send_keys('')
        self.driver.find_element(By.NAME, 'password1').send_keys('pass12345')
        self.driver.find_element(By.NAME, 'password2').send_keys('pass12345')
        self.driver.find_element(By.ID, 'registerButton').click()
        self.assertEqual(self.driver.title, 'Registering')

    ## Test register feature with empty password
    def test_register_feature_empty_password(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'registerLink').click()
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'first_name').send_keys('first')
        self.driver.find_element(By.NAME, 'last_name').send_keys('last')
        self.driver.find_element(By.NAME, 'email').send_keys('test@email.com')
        self.driver.find_element(By.NAME, 'phone_number').send_keys('1-222-333-4444')
        self.driver.find_element(By.NAME, 'password1').send_keys('')
        self.driver.find_element(By.NAME, 'password2').send_keys('pass12345')
        self.driver.find_element(By.ID, 'registerButton').click()
        self.assertEqual(self.driver.title, 'Registering')

    ## Test register feature with empty confirmation password
    def test_register_feature_empty_confirm_password(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'registerLink').click()
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'first_name').send_keys('first')
        self.driver.find_element(By.NAME, 'last_name').send_keys('last')
        self.driver.find_element(By.NAME, 'email').send_keys('test@email.com')
        self.driver.find_element(By.NAME, 'phone_number').send_keys('1-222-333-4444')
        self.driver.find_element(By.NAME, 'password1').send_keys('pass12345')
        self.driver.find_element(By.NAME, 'password2').send_keys('')
        self.driver.find_element(By.ID, 'registerButton').click()
        self.assertEqual(self.driver.title, 'Registering')

    ## Test register feature with email too long
    def test_register_feature_email_too_long(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'registerLink').click()
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'first_name').send_keys('first')
        self.driver.find_element(By.NAME, 'last_name').send_keys('last')
        self.driver.find_element(By.NAME, 'email').send_keys(('test' * 150) + '@email.com')
        self.driver.find_element(By.NAME, 'phone_number').send_keys('1-222-333-4444')
        self.driver.find_element(By.NAME, 'password1').send_keys('pass12345')
        self.driver.find_element(By.NAME, 'password2').send_keys('pass12345')
        self.driver.find_element(By.ID, 'registerButton').click()
        self.assertEqual(self.driver.title, 'Registering')

    ## Test register feature with incorrectly formatted email
    def test_register_feature_incorrectly_formatted_email(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'registerLink').click()
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'first_name').send_keys('first')
        self.driver.find_element(By.NAME, 'last_name').send_keys('last')
        self.driver.find_element(By.NAME, 'email').send_keys('testatemail.com')
        self.driver.find_element(By.NAME, 'phone_number').send_keys('1-222-333-4444')
        self.driver.find_element(By.NAME, 'password1').send_keys('pass12345')
        self.driver.find_element(By.NAME, 'password2').send_keys('pass12345')
        self.driver.find_element(By.ID, 'registerButton').click()
        self.assertEqual(self.driver.title, 'Registering')

    ## Test register feature with invalid password
    def test_register_feature_invalid_password(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'registerLink').click()
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'first_name').send_keys('first')
        self.driver.find_element(By.NAME, 'last_name').send_keys('last')
        self.driver.find_element(By.NAME, 'email').send_keys('test@email.com')
        self.driver.find_element(By.NAME, 'phone_number').send_keys('1-222-333-4444')
        self.driver.find_element(By.NAME, 'password1').send_keys('test')
        self.driver.find_element(By.NAME, 'password2').send_keys('test')
        self.driver.find_element(By.ID, 'registerButton').click()
        self.assertEqual(self.driver.title, 'Registering')

    ## Test register feature with mismatching passwords
    def test_register_feature_mismatching_passwords(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'registerLink').click()
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'first_name').send_keys('first')
        self.driver.find_element(By.NAME, 'last_name').send_keys('last')
        self.driver.find_element(By.NAME, 'email').send_keys('test@email.com')
        self.driver.find_element(By.NAME, 'phone_number').send_keys('1-222-333-4444')
        self.driver.find_element(By.NAME, 'password1').send_keys('mismatching')
        self.driver.find_element(By.NAME, 'password2').send_keys('passwords')
        self.driver.find_element(By.ID, 'registerButton').click()
        self.assertEqual(self.driver.title, 'Registering')

    ## Test register feature success
    def test_register_feature_success(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'registerLink').click()
        self.driver.find_element(By.NAME, 'username').send_keys('test')
        self.driver.find_element(By.NAME, 'first_name').send_keys('first')
        self.driver.find_element(By.NAME, 'last_name').send_keys('last')
        self.driver.find_element(By.NAME, 'email').send_keys('test@email.com')
        self.driver.find_element(By.NAME, 'phone_number').send_keys('1-222-333-4444')
        self.driver.find_element(By.NAME, 'password1').send_keys('pass12345')
        self.driver.find_element(By.NAME, 'password2').send_keys('pass12345')
        self.driver.find_element(By.ID, 'registerButton').click()
        self.assertEqual(self.driver.title, 'Home')
