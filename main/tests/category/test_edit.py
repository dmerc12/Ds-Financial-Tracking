from tests.category.POMs.edit import edit_deposit_category, edit_expense_category
from selenium.webdriver.edge.webdriver import WebDriver
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from users.models import CustomUser

# Tests for edit category feature
class EditCategoryTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    ## Test edit deposit category feature with empty name
    def test_edit_deposit_category_feature_empty_name(self):
        edit_deposit_category(self, 'Updating Category', self.user.username, self.password, 'test', '')

    ## Test edit deposit category feature with name too long
    def test_edit_deposit_category_feature_name_too_long(self):
        edit_deposit_category(self, 'Updating Category', self.user.username, self.password, 'test', 'updated' * 61)

    ## Test edit deposit category feature with success
    def test_edit_deposit_category_feature_success(self):
        edit_deposit_category(self, 'Managing Deposits', self.user.username, self.password, 'test', 'updated')

    ## Test edit expense category feature with empty name
    def test_edit_expense_category_feature_empty_name(self):
        edit_expense_category(self, 'Updating Category', self.user.username, self.password, 'test', '')

    ## Test edit expense category feature with name too long
    def test_edit_expense_category_feature_name_too_long(self):
        edit_expense_category(self, 'Updating Category', self.user.username, self.password, 'test', 'updated' * 61)

    ## Test edit expense category feature with success
    def test_edit_expense_category_feature_success(self):
        edit_expense_category(self, 'Managing Expenses', self.user.username, self.password, 'test', 'updated')
