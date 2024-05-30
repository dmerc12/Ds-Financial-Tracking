from selenium.webdriver.edge.webdriver import WebDriver
from tests.expense.POMs.create import create_expense
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from users.models import CustomUser
from datetime import datetime

# Tests for create expense feature
class CreateExpenseTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    ## Test create expense feature with empty category
    def test_create_expense_feature_category_empty(self):
        create_expense(self, 'Creating Expense', self.user.username, self.password, 'category name', 0, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62)

    ## Test create expense feature with empty date
    def test_create_expense_feature_empty_date(self):
        create_expense(self, 'Creating Expense', self.user.username, self.password, 'category name', 1, '', 'description', 45.62)

    ## Test create expense feature with description empty
    def test_create_expense_feature_empty_description(self):
        create_expense(self, 'Creating Expense', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), '', 45.62)

    ## Test create expense feature with empty amount
    def test_create_expense_feature_empty_amount(self):
        create_expense(self, 'Creating Expense', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', '')

    ## Test create expense feature with negative amount
    def test_create_expense_feature_negative_amount(self):
        create_expense(self, 'Creating Expense', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', -45.62)

    ## Test create expense feature success
    def test_create_expense_feature_success(self):
        create_expense(self, 'Managing Expenses', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62)
