from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
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
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'trackFinancesButton').click()
        self.driver.find_element(By.ID, 'depositHomeLink').click()
        self.driver.find_element(By.ID, 'createCategoryLink').click()
        self.driver.find_element(By.NAME, 'name').send_keys('')
        self.driver.find_element(By.ID, 'createCategoryButton').click()
        self.assertEqual(self.driver.title, 'Adding Category')

    ## Test create deposit category feature with name too long
    def test_create_deposit_category_feature_name_too_long(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'trackFinancesButton').click()
        self.driver.find_element(By.ID, 'depositHomeLink').click()
        self.driver.find_element(By.ID, 'createCategoryLink').click()
        self.driver.find_element(By.NAME, 'name').send_keys('t' * 61)
        self.driver.find_element(By.ID, 'createCategoryButton').click()
        self.assertEqual(self.driver.title, 'Adding Category')

    ## Test create deposit category feature success
    def test_create_deposit_category_feature_success(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'trackFinancesButton').click()
        self.driver.find_element(By.ID, 'depositHomeLink').click()
        self.driver.find_element(By.ID, 'createCategoryLink').click()
        self.driver.find_element(By.NAME, 'name').send_keys('test')
        self.driver.find_element(By.ID, 'createCategoryButton').click()
        self.assertEqual(self.driver.title, 'Managing Deposits')

    ## Test create expense category feature with empty name
    def test_create_expense_category_feature_empty_name(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'trackFinancesButton').click()
        self.driver.find_element(By.ID, 'expenseHomeLink').click()
        self.driver.find_element(By.ID, 'createCategoryLink').click()
        self.driver.find_element(By.NAME, 'name').send_keys('')
        self.driver.find_element(By.ID, 'createCategoryButton').click()
        self.assertEqual(self.driver.title, 'Adding Category')

    ## Test create expense category feature with name too long
    def test_create_expense_category_feature_name_too_long(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'trackFinancesButton').click()
        self.driver.find_element(By.ID, 'expenseHomeLink').click()
        self.driver.find_element(By.ID, 'createCategoryLink').click()
        self.driver.find_element(By.NAME, 'name').send_keys('t' * 61)
        self.driver.find_element(By.ID, 'createCategoryButton').click()
        self.assertEqual(self.driver.title, 'Adding Category')

    ## Test create expense category feature success
    def test_create_expense_category_feature_success(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'trackFinancesButton').click()
        self.driver.find_element(By.ID, 'expenseHomeLink').click()
        self.driver.find_element(By.ID, 'createCategoryLink').click()
        self.driver.find_element(By.NAME, 'name').send_keys('test')
        self.driver.find_element(By.ID, 'createCategoryButton').click()
        self.assertEqual(self.driver.title, 'Managing Expenses')
