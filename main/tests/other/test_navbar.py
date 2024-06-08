from selenium.webdriver.edge.webdriver import WebDriver
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from tests.other.POMs import navbar
from users.models import CustomUser

# Tests for create expense feature
class NavbarTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    def test_home_tab_redirect(self):
        navbar.home_redirect(self, 'Log In')

    def test_home_tab(self):
        navbar.home_success(self, 'Home', self.user.username, self.password)

    def test_manage_info_redirect(self):
        navbar.manage_info_redirect(self, 'Log In')

    def test_manage_info_success(self):
        navbar.manage_info_success(self, 'Updating Information', self.user.username, self.password)

    def test_manage_deposits_redirect(self):
        navbar.manage_deposits_redirect(self, 'Log In')

    def test_manage_deposits_success(self):
        navbar.manage_deposits_success(self, 'Managing Deposits', self.user.username, self.password)

    def test_manage_expenses_redirect(self):
        navbar.manage_expenses_redirect(self, 'Log In')

    def test_manage_expenses_success(self):
        navbar.manage_expenses_success(self, 'Managing Expenses', self.user.username, self.password)

    def test_view_finances_redirect(self):
        navbar.view_finances_redirect(self, 'Log In')

    def test_view_finances_success(self):
        navbar.view_finances_success(self, 'Viewing Finances', self.user.username, self.password)

    def test_analyze_finances_redirect(self):
        navbar.analyze_finances_redirect(self, 'Log In')

    def test_analyze_finances_success(self):
        navbar.analyze_finances_success(self, 'Analyzing Finances', self.user.username, self.password)

    def test_logout(self):
        navbar.logout(self, 'Log In', self.user.username, self.password)
