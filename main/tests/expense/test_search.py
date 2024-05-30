from selenium.webdriver.edge.webdriver import WebDriver
from tests.expense.POMs.search import expense_search
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from datetime import datetime, timedelta
from users.models import CustomUser

# Tests for expense search feature
class ExpenseSearchTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    ## Test expense search feature success with expense ID
    def test_expense_search_feature_success_expense_id(self):
        expense_search(self, 'Managing Expenses', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, 9, '', '')

    ## Test expense search feature success with start date
    def test_expense_search_feature_success_start_date(self):
        expense_search(self, 'Managing Expenses', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, '', (datetime.now() - timedelta(weeks=8)).strftime('%m-%d-%Y'), '')

    ## Test expense search feature success with start and end date
    def test_expense_search_feature_success_start_and_end_dates(self):
        expense_search(self, 'Managing Expenses', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, '', (datetime.now() - timedelta(weeks=8)).strftime('%m-%d-%Y'), datetime.now().strftime('%m-%d-%Y'))
