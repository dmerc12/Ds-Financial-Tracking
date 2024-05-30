from selenium.webdriver.edge.webdriver import WebDriver
from django.contrib.auth.models import User
from tests.users.POMs.edit import edit_user
from django.test import LiveServerTestCase
from users.models import CustomUser

# Tests for edit user feature
class EditUserTests(LiveServerTestCase):

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

    ## Test edit user feature with empty username
    def test_edit_user_feature_empty_username(self):
        edit_user(self, 'Updating Information', self.user.username, self.password, '', 'updated first', 'updated_last', 'updated@email.com', '4-333-222-1111')

    ## Test edit user feature with empty first name
    def test_edit_user_feature_empty_first_name(self):
        edit_user(self, 'Updating Information', self.user.username, self.password, 'updated', '', 'updated_last', 'updated@email.com', '4-333-222-1111')

    ## Test edit user feature with empty last name
    def test_edit_user_feature_empty_last_name(self):
        edit_user(self, 'Updating Information', self.user.username, self.password, 'updated', 'updated first', '', 'updated@email.com', '4-333-222-1111')

    ## Test edit user feature with empty email
    def test_edit_user_feature_empty_email(self):
        edit_user(self, 'Updating Information', self.user.username, self.password, 'updated', 'updated first', 'updated_last', '', '4-333-222-1111')

    ## Test edit user feature with empty phone number
    def test_edit_user_feature_empty_phone_number(self):
        edit_user(self, 'Updating Information', self.user.username, self.password, 'updated', 'updated first', 'updated_last', 'updated@email.com', '')

    ## Test edit user feature with first name too long
    def test_edit_user_feature_first_name_too_long(self):
        edit_user(self, 'Updating Information', self.user.username, self.password, 'updated', 'test' * 100, 'updated_last', 'updated@email.com', '4-333-222-1111')

    ## Test edit user feature with last name too long
    def test_edit_user_feature_last_name_too_long(self):
        edit_user(self, 'Updating Information', self.user.username, self.password, 'updated', 'updated first', 'test' * 100, 'updated@email.com', '4-333-222-1111')

    ## Test edit user feature with email too long
    def test_edit_user_feature_email_too_long(self):
        edit_user(self, 'Updating Information', self.user.username, self.password, 'updated', 'updated first', 'updated_last', 'test' * 150 + '@email.com', '4-333-222-1111')

    ## Test edit user feature with email incorrectly formatted
    def test_edit_user_feature_email_incorrect_format(self):
        edit_user(self, 'Updating Information', self.user.username, self.password, 'updated', 'updated first', 'updated_last', 'incorrect format', '4-333-222-1111')

    ## Test edit user feature success
    def test_edit_user_feature_success(self):
        edit_user(self, 'Home', self.user.username, self.password, 'updated', 'updated first', 'updated_last', 'updated@email.com', '4-333-222-1111')
