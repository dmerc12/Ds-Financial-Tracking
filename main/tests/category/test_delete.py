from tests.category.POMs.delete import delete_deposit_category, delete_expense_category
from selenium.webdriver.edge.webdriver import WebDriver
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from users.models import CustomUser

# Tests for delete category feature
class DeleteCategoryTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    ## Test delete deposit category feature with success
    def test_delete_deposit_category_feature_success(self):
        delete_deposit_category(self, 'Managing Deposits', self.user.username, self.password, 'test')

    ## Test delete expense category feature with success
    def test_delete_expense_category_feature_success(self):
        delete_expense_category(self, 'Managing Expenses', self.user.username, self.password, 'test')
