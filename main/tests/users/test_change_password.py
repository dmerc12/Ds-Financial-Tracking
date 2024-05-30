from tests.users.POMs.change_password import change_password
from selenium.webdriver.edge.webdriver import WebDriver
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from users.models import CustomUser

# Tests for change password feature
class ChangePasswordTests(LiveServerTestCase):

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

    ## Test change password feature with empty password
    def test_change_password_feature_empty_password(self):
        change_password(self, 'Changing Password', self.user.username, self.password, '', 'new_pass12345')

    ## Test change password  feature with empty confirmation passwod
    def test_change_password_feature_empty_confirm_password(self):
        change_password(self, 'Changing Password', self.user.username, self.password, 'new_pass12345', '')

    ## Test change password feature with invalid passwords
    def test_change_password_feature_invalid_passwords(self):
        change_password(self, 'Changing Password', self.user.username, self.password, 'test', 'test')

    ## Test change password feature with mismatching passwords
    def test_change_password_feature_mismatching_passwords(self):
        change_password(self, 'Changing Password', self.user.username, self.password, 'mismatching', 'passwords')

    ## Test change password feature success
    def test_change_password_feature_success(self):
        change_password(self, 'Home', self.user.username, self.password, 'new_pass12345', 'new_pass12345')
