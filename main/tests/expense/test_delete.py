from selenium.webdriver.edge.webdriver import WebDriver
from tests.expense.POMs.delete import delete_expense
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from users.models import CustomUser
from datetime import datetime

# Tests for delete expense feature
class DeleteExpenseTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    ## Test delete expense feature success
    def test_delete_expense_feature_success(self):
        delete_expense(self, 'Managing Expenses', self.user.username, self.password, 'category name', 1, datetime.now().strftime('%m-%d-%Y'), 'description', 45.62, 2)
