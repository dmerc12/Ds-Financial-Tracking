from selenium.webdriver.edge.webdriver import WebDriver
from tests.expense.POMs.edit import edit_expense
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from users.models import CustomUser
from datetime import datetime

# Tests for edit expense feature
class EditDepositTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    ## Test edit expense feature with empty category
    def test_edit_expense_feature_empty_category(self):
        edit_expense(self, 'Updating Expense', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, 4, 0, datetime.now().strftime('%m-%d-%Y'), 'updated description', 78.56)

    ## Test edit expense feature with empty date
    def test_edit_expense_feature_empty_date(self):
        edit_expense(self, 'Updating Expense', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, 5, 1, '', 'updated description', 78.56)

    ## Test edit expense feature with empty description
    def test_edit_expense_feature_empty_description(self):
        edit_expense(self, 'Updating Expense', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, 6, 1, datetime.now().strftime('%m-%d-%Y'), '', 78.56)

    ## Test edit expense feature with empty amount
    def test_edit_expense_feature_empty_amount(self):
        edit_expense(self, 'Updating Expense', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, 3, 1, datetime.now().strftime('%m-%d-%Y'), 'updated description', '')

    ## Test edit expense feature with negative amount
    def test_edit_expense_feature_negative_amount(self):
        edit_expense(self, 'Updating Expense', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, 7, 1, datetime.now().strftime('%m-%d-%Y'), 'updated description', -78.56)

    ## Test edit expense feature success
    def test_edit_expense_feature_success(self):
        edit_expense(self, 'Managing Expenses', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, 8, 1, datetime.now().strftime('%m-%d-%Y'), 'updated description', 78.56)
