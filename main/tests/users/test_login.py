from selenium.webdriver.edge.webdriver import WebDriver
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from tests.users.POMs.login import login
from users.models import CustomUser

# Tests for login feature
class LoginTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test', password=self.password, first_name='first', last_name='last', email='test@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    def tearDown(self):
        self.driver.close()
        User.objects.all().delete()
        CustomUser.objects.all().delete()

    ## Test login feature with empty username
    def test_login_feature_empty_username(self):
        login(self, 'Log In', '', 'pass12345')

    ## Test login feature with empty password
    def test_login_feature_empty_password(self):
        login(self, 'Log In', 'test', '')

    ## Test login feature with username too long
    def test_login_feature_username_too_long(self):
        login(self, 'Log In', 'test' * 150, 'pass12345')

    ## Test login feature with incorrect credentials
    def test_login_feature_incorrect_credentials(self):
        login(self, 'Log In', 'incorrect', 'credentials')

    ## Test login feature success
    def test_login_feature_success(self):
        login(self, 'Home', 'test', 'pass12345')
