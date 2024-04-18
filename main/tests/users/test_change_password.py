from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from users.models import CustomUser

# Tests for change password feature
class ChangePasswordTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    def tearDown(self):
        self.driver.close()
        User.objects.all().delete()
        CustomUser.objects.all().delete()

    ## Test change password feature with empty password
    def test_change_password_feature_empty_password(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'manageInfoButton').click()
        self.driver.find_element(By.ID, 'changePasswordLink').click()
        self.driver.find_element(By.NAME, 'new_password1').send_keys('')
        self.driver.find_element(By.NAME, 'new_password2').send_keys('new_pass12345')
        self.driver.find_element(By.ID, 'changePasswordButton').click()
        self.assertEqual(self.driver.title, 'Changing Password')

    ## Test change password  feature with empty confirmation passwod
    def test_change_password_feature_empty_confirm_password(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'manageInfoButton').click()
        self.driver.find_element(By.ID, 'changePasswordLink').click()
        self.driver.find_element(By.NAME, 'new_password1').send_keys('new_pass12345')
        self.driver.find_element(By.NAME, 'new_password2').send_keys('')
        self.driver.find_element(By.ID, 'changePasswordButton').click()
        self.assertEqual(self.driver.title, 'Changing Password')

    ## Test change password feature with invalid passwords
    def test_change_password_feature_invalid_passwords(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'manageInfoButton').click()
        self.driver.find_element(By.ID, 'changePasswordLink').click()
        self.driver.find_element(By.NAME, 'new_password1').send_keys('test1')
        self.driver.find_element(By.NAME, 'new_password2').send_keys('test1')
        self.driver.find_element(By.ID, 'changePasswordButton').click()
        self.assertEqual(self.driver.title, 'Changing Password')

    ## Test change password feature with mismatching passwords
    def test_change_password_feature_mismatching_passwords(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'manageInfoButton').click()
        self.driver.find_element(By.ID, 'changePasswordLink').click()
        self.driver.find_element(By.NAME, 'new_password1').send_keys('mismatching')
        self.driver.find_element(By.NAME, 'new_password2').send_keys('passwords')
        self.driver.find_element(By.ID, 'changePasswordButton').click()
        self.assertEqual(self.driver.title, 'Changing Password')

    ## Test change password feature success
    def test_change_password_feature_success(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'manageInfoButton').click()
        self.driver.find_element(By.ID, 'changePasswordLink').click()
        self.driver.find_element(By.NAME, 'new_password1').send_keys('new_pass12345')
        self.driver.find_element(By.NAME, 'new_password2').send_keys('new_pass12345')
        self.driver.find_element(By.ID, 'changePasswordButton').click()
        self.assertEqual(self.driver.title, 'Home')
