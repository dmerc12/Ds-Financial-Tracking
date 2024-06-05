from selenium.webdriver.edge.webdriver import WebDriver
from tests.deposit.POMs.delete import delete_deposit
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from users.models import CustomUser
from datetime import datetime

# Tests for delete deposit feature
class DeleteDepositTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    ## Test delete deposit feature success
    def test_delete_deposit_feature_success(self):
        delete_deposit(self, 'Managing Deposits', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, 2)
