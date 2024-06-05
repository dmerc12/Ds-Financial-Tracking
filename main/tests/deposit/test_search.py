from selenium.webdriver.edge.webdriver import WebDriver
from tests.deposit.POMs.search import deposit_search
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from datetime import datetime, timedelta
from users.models import CustomUser

# Tests for deposit search feature
class DepositSearchTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    ## Test deposit search feature success with deposit ID
    def test_deposit_search_feature_success_deposit_id(self):
        deposit_search(self, 'Managing Deposits', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, 9, '', '')

    ## Test deposit search feature success with start date
    def test_deposit_search_feature_success_start_date(self):
        deposit_search(self, 'Managing Deposits', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, '', (datetime.now() - timedelta(weeks=8)).strftime('%m-%d-%Y'), '')

    ## Test deposit search feature success with start and end date
    def test_deposit_search_feature_success_start_and_end_dates(self):
        deposit_search(self, 'Managing Deposits', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, '', (datetime.now() - timedelta(weeks=8)).strftime('%m-%d-%Y'), datetime.now().strftime('%m-%d-%Y'))
