from selenium.webdriver.edge.webdriver import WebDriver
from tests.users.POMs.delete import delete_user
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
        delete_user(self, 'Log In', self.user.username, self.password)
