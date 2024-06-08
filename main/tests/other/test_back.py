from selenium.webdriver.edge.webdriver import WebDriver
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from users.models import CustomUser
from tests.other.POMs import back

# Tests for back buttons feature
class BackTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    def test_change_password_back(self):
        back.change_password_back(self, 'Updating Information', self.user.username, self.password)

    def test_delete_user_back(self):
        back.delete_user_back(self, 'Updating Information', self.user.username, self.password)

    def test_create_deposit_category_back(self):
        back.create_deposit_category_back(self, 'Managing Deposits', self.user.username, self.password)

    def test_update_deposit_category_back(self):
        back.update_deposit_category_back(self, 'Managing Deposits', self.user.username, self.password)

    def test_delete_deposit_category_back(self):
        back.delete_deposit_category_back(self, 'Managing Deposits', self.user.username, self.password)

    def test_create_deposit_back(self):
        back.create_deposit_back(self, 'Managing Deposits', self.user.username, self.password)

    def test_deposit_detail_back(self):
        back.deposit_detail_back(self, 'Managing Deposits', self.user.username, self.password)

    def test_update_deposit_back(self):
        back.update_deposit_back(self, 'Deposit - 14', self.user.username, self.password)

    def test_delete_deposit_back(self):
        back.delete_deposit_back(self, 'Deposit - 12', self.user.username, self.password)

    def test_create_expense_category_back(self):
        back.create_expense_category_back(self, 'Managing Expenses', self.user.username, self.password)

    def test_update_expense_category_back(self):
        back.update_expense_category_back(self, 'Managing Expenses', self.user.username, self.password)

    def test_delete_expense_category_back(self):
        back.delete_expense_category_back(self, 'Managing Expenses', self.user.username, self.password)

    def test_create_expense_back(self):
        back.create_expense_back(self, 'Managing Expenses', self.user.username, self.password)

    def test_expense_detail_back(self):
        back.expense_detail_back(self, 'Managing Expenses', self.user.username, self.password)

    def test_update_expense_back(self):
        back.update_expense_back(self, 'Expense - 14', self.user.username, self.password)

    def test_delete_expense_back(self):
        back.delete_expense_back(self, 'Expense - 12', self.user.username, self.password)
