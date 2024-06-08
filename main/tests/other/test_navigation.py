from selenium.webdriver.edge.webdriver import WebDriver
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from tests.other.POMs import navigation
from users.models import CustomUser

# Tests for create expense feature
class NavigationTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    def test_sign_up_link(self):
        navigation.navigate_sign_up_link(self, 'Registering')

    def test_log_in_link(self):
        navigation.navigate_log_in_link(self, 'Log In')

    def test_navigate_manage_info(self):
        navigation.navigate_manage_info(self, 'Updating Information', self.user.username, self.password)

    def test_navigate_change_password(self):
        navigation.navigate_change_password(self, 'Changing Password', self.user.username, self.password)

    def test_navigate_delete_user(self):
        navigation.navigate_delete_user(self, 'Deleting Account', self.user.username, self.password)

    def test_navigate_track_finances(self):
        navigation.navigate_track_finances(self, 'Finance Tracking Home', self.user.username, self.password)

    def test_navigate_create_deposit_category(self):
        navigation.navigate_create_deposit_category(self, 'Adding Category', self.user.username, self.password)

    def test_navigate_update_deposit_category(self):
        navigation.navigate_update_deposit_category(self, 'Updating Category', self.user.username, self.password)

    def test_navigate_delete_deposit_category(self):
        navigation.navigate_delete_deposit_category(self, 'Deleting Category', self.user.username, self.password)

    def test_navigate_create_expense_category(self):
        navigation.navigate_create_expense_category(self, 'Adding Category', self.user.username, self.password)

    def test_navigate_update_expense_category(self):
        navigation.navigate_update_expense_category(self, 'Updating Category', self.user.username, self.password)

    def test_navigate_delete_expense_category(self):
        navigation.navigate_delete_expense_category(self, 'Deleting Category', self.user.username, self.password)

    def test_navigate_manage_deposits(self):
        navigation.navigate_manage_deposits(self, 'Managing Deposits', self.user.username, self.password)

    def test_navigate_deposit_detail(self):
        ID = 13
        navigation.navigate_deposit_detail(self, f'Deposit - {ID}', self.user.username, self.password, ID)

    def test_navigate_create_deposit(self):
        navigation.navigate_create_deposit(self, 'Creating Deposit', self.user.username, self.password)

    def test_navigate_update_deposit(self):
        navigation.navigate_update_deposit(self, 'Updating Deposit', self.user.username, self.password, 14)

    def test_navigate_delete_deposit(self):
        navigation.navigate_delete_deposit(self, 'Deleting Deposit', self.user.username, self.password, 12)

    def test_navigate_manage_expenses(self):
        navigation.navigate_manage_expenses(self, 'Managing Expenses', self.user.username, self.password)

    def test_navigate_expense_detail(self):
        ID = 13
        navigation.navigate_expense_detail(self, f'Expense - {ID}', self.user.username, self.password, ID)

    def test_navigate_create_expense(self):
        navigation.navigate_create_expense(self, 'Creating Expense', self.user.username, self.password)

    def test_navigate_update_expense(self):
        navigation.navigate_update_expense(self, 'Updating Expense', self.user.username, self.password, 14)

    def test_navigate_delete_expense(self):
        navigation.navigate_delete_expense(self, 'Deleting Expense', self.user.username, self.password, 12)

    def test_navigate_view_finances(self):
        navigation.navigate_view_finances(self, 'Viewing Finances', self.user.username, self.password)

    def test_navigate_analyze_finances(self):
        navigation.navigate_analyze_finances(self, 'Analyzing Finances', self.user.username, self.password)
