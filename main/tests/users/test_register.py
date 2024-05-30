from selenium.webdriver.edge.webdriver import WebDriver
from tests.users.POMs.register import register
from django.test import LiveServerTestCase

# Tests for register feature
class RegisterTests(LiveServerTestCase):

    def setUp(self):
        self.driver = WebDriver()

    def tearDown(self):
        self.driver.close()

    ## Test register feature with empty username
    def test_register_feature_empty_username(self):
        register(self, 'Registering', '', 'first', 'last', 'test@email.com', '1-222-333-4444', 'pass12345', 'pass12345')

    ## Test register feature with empty first name
    def test_register_feature_empty_first_name(self):
        register(self, 'Registering', 'test', '', 'last', 'test@email.com', '1-222-333-4444', 'pass12345', 'pass12345')

    ## Test register feature with empty last name
    def test_register_feature_empty_last_name(self):
        register(self, 'Registering', 'test', 'first', '', 'test@email.com', '1-222-333-4444', 'pass12345', 'pass12345')

    ## Test register feature with empty email
    def test_register_feature_empty_email(self):
        register(self, 'Registering', 'test', 'first', 'last', '', '1-222-333-4444', 'pass12345', 'pass12345')

    ## Test register feature with empty phone number
    def test_register_feature_empty_phone_number(self):
        register(self, 'Registering', 'test', 'first', 'last', 'test@email.com', '', 'pass12345', 'pass12345')

    ## Test register feature with empty password
    def test_register_feature_empty_password(self):
        register(self, 'Registering', 'test', 'first', 'last', 'test@email.com', '1-222-333-4444', '', 'pass12345')

    ## Test register feature with empty confirmation password
    def test_register_feature_empty_confirm_password(self):
        register(self, 'Registering', 'test', 'first', 'last', 'test@email.com', '1-222-333-4444', 'pass12345', '')

    ## Test register feature with email too long
    def test_register_feature_email_too_long(self):
        register(self, 'Registering', 'test', 'first', 'last', 'test' * 150 + '@email.com', '1-222-333-4444', 'pass12345', 'pass12345')

    ## Test register feature with incorrectly formatted email
    def test_register_feature_incorrectly_formatted_email(self):
        register(self, 'Registering', 'test', 'first', 'last', 'incorrect format', '1-222-333-4444', 'pass12345', 'pass12345')

    ## Test register feature with invalid password
    def test_register_feature_invalid_password(self):
        register(self, 'Registering', 'test', 'first', 'last', 'test@email.com', '1-222-333-4444', 'test', 'test')

    ## Test register feature with mismatching passwords
    def test_register_feature_mismatching_passwords(self):
        register(self, 'Registering', 'test', 'first', 'last', 'test@email.com', '1-222-333-4444', 'mismatching', 'passwords')

    ## Test register feature success
    def test_register_feature_success(self):
        register(self, 'Home', 'test', 'first', 'last', 'test@email.com', '1-222-333-4444', 'pass12345', 'pass12345')
