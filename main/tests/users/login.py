from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from users.models import CustomUser

# Tests for login feature
class LoginTests(LiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test1', password='pass12345', first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')
        self.driver = WebDriver()

    ## Test login feature with empty username
    def test_login_feature_empty_username(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'username').send_keys('')
        self.driver.find_element(By.ID, 'password').send_keys('pass12345')
        self.driver.find_element(By.ID, 'loginButton').click()
        self.assertEqual(self.driver.title, 'Log In')

    ## Test login feature with empty password
    def test_login_feature_empty_password(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'username').send_keys('test')
        self.driver.find_element(By.ID, 'password').send_keys('')
        self.driver.find_element(By.ID, 'loginButton').click()
        self.assertEqual(self.driver.title, 'Log In')

    ## Test login feature with username too long
    def test_login_feature_username_too_long(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'username').send_keys('t' * 151)
        self.driver.find_element(By.ID, 'password').send_keys('pass12345')
        self.driver.find_element(By.ID, 'loginButton').click()
        self.assertEqual(self.driver.title, 'Log In')

    ## Test login feature with incorrect credentials
    def test_login_feature_incorrect_credentials(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'username').send_keys('incorrect')
        self.driver.find_element(By.ID, 'password').send_keys('credentials')
        self.driver.find_element(By.ID, 'loginButton').click()
        self.assertEqual(self.driver.title, 'Log In')

    ## Test login feature success
    def test_login_feature_success(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.ID, 'username').send_keys(self.user.username)
        self.driver.find_element(By.ID, 'password').send_keys(self.user.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.assertEqual(self.driver.title, 'Home')
