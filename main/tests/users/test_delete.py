from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from users.models import CustomUser

# Tests for delete user feature
class DeleteUserTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    ## Test delete user feature success
    def test_delete_user_feature_success(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'manageInfoButton').click()
        self.driver.find_element(By.ID, 'deleteUserLink').click()
        self.driver.find_element(By.ID, 'deleteUserButton').click()
        self.assertEqual(self.driver.title, 'Log In')
