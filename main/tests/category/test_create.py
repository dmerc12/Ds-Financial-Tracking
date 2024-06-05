from tests.category.POMs.create import create_deposit_category, create_expense_category
from selenium.webdriver.edge.webdriver import WebDriver
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from users.models import CustomUser

# Tests for create category feature
class CreateCategoryTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    ## Test create deposit category feature with empty name
    def test_create_deposit_category_feature_empty_name(self):
        create_deposit_category(self, 'Adding Category', self.user.username, self.password, '')

    ## Test create deposit category feature with name too long
    def test_create_deposit_category_feature_name_too_long(self):
        create_deposit_category(self, 'Adding Category', self.user.username, self.password, 'test' * 61)

    ## Test create deposit category feature success
    def test_create_deposit_category_feature_success(self):
        create_deposit_category(self, 'Managing Deposits', self.user.username, self.password, 'test')

    ## Test create expense category feature with empty name
    def test_create_expense_category_feature_empty_name(self):
        create_expense_category(self, 'Adding Category', self.user.username, self.password, '')

    ## Test create expense category feature with name too long
    def test_create_expense_category_feature_name_too_long(self):
        create_expense_category(self, 'Adding Category', self.user.username, self.password, 'test' * 61)

    ## Test create expense category feature success
    def test_create_expense_category_feature_success(self):
        create_expense_category(self, 'Managing Expenses', self.user.username, self.password, 'test')
