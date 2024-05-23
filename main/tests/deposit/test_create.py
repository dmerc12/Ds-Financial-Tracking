from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from users.models import CustomUser
from datetime import datetime

# Tests for create deposit feature
class CreateDepositTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    ## Test create deposit feature with empty category
    def test_create_deposit_feature_category_empty(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'trackFinancesButton').click()
        self.driver.find_element(By.ID, 'depositHomeLink').click()
        self.driver.find_element(By.ID, 'createCategoryLink').click()
        self.driver.find_element(By.NAME, 'name').send_keys('test')
        self.driver.find_element(By.ID, 'createCategoryButton').click()
        self.driver.find_element(By.ID, 'createDepositLink').click()
        self.driver.find_element(By.NAME, 'date').send_keys(datetime.now().strftime('%m-%d-%Y'))
        self.driver.find_element(By.NAME, 'description').send_keys('description')
        self.driver.find_element(By.NAME, 'amount').send_keys(45.62)
        self.driver.find_element(By.ID, 'createDepositButton').click()
        self.assertEqual(self.driver.title, 'Create Deposit')

    ## Test create deposit feature with empty date
    def test_create_deposit_feature_empty_date(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'trackFinancesButton').click()
        self.driver.find_element(By.ID, 'depositHomeLink').click()
        self.driver.find_element(By.ID, 'createCategoryLink').click()
        self.driver.find_element(By.NAME, 'name').send_keys('test')
        self.driver.find_element(By.ID, 'createCategoryButton').click()
        self.driver.find_element(By.ID, 'createDepositLink').click()
        category_dropdown = self.driver.find_element(By.NAME, 'category')
        category_select = Select(category_dropdown)
        category_select.select_by_index(1)
        self.driver.find_element(By.NAME, 'description').send_keys('description')
        self.driver.find_element(By.NAME, 'amount').send_keys(45.62)
        self.driver.find_element(By.ID, 'createDepositButton').click()
        self.assertEqual(self.driver.title, 'Create Deposit')

    ## Test create deposit feature with description empty
    def test_create_deposit_feature_empty_description(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'trackFinancesButton').click()
        self.driver.find_element(By.ID, 'depositHomeLink').click()
        self.driver.find_element(By.ID, 'createCategoryLink').click()
        self.driver.find_element(By.NAME, 'name').send_keys('test')
        self.driver.find_element(By.ID, 'createCategoryButton').click()
        self.driver.find_element(By.ID, 'createDepositLink').click()
        category_dropdown = self.driver.find_element(By.NAME, 'category')
        category_select = Select(category_dropdown)
        category_select.select_by_index(1)
        self.driver.find_element(By.NAME, 'date').send_keys(datetime.now().strftime('%m-%d-%Y'))
        self.driver.find_element(By.NAME, 'amount').send_keys(45.62)
        self.driver.find_element(By.ID, 'createDepositButton').click()
        self.assertEqual(self.driver.title, 'Create Deposit')

    ## Test create deposit feature with empty amount
    def test_create_deposit_feature_empty_amount(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'trackFinancesButton').click()
        self.driver.find_element(By.ID, 'depositHomeLink').click()
        self.driver.find_element(By.ID, 'createCategoryLink').click()
        self.driver.find_element(By.NAME, 'name').send_keys('test')
        self.driver.find_element(By.ID, 'createCategoryButton').click()
        self.driver.find_element(By.ID, 'createDepositLink').click()
        category_dropdown = self.driver.find_element(By.NAME, 'category')
        category_select = Select(category_dropdown)
        category_select.select_by_index(1)
        self.driver.find_element(By.NAME, 'date').send_keys(datetime.now().strftime('%m-%d-%Y'))
        self.driver.find_element(By.NAME, 'description').send_keys('description')
        self.driver.find_element(By.ID, 'createDepositButton').click()
        self.assertEqual(self.driver.title, 'Create Deposit')

    ## Test create deposit feature with negative amount
    def test_create_deposit_feature_negative_amount(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'trackFinancesButton').click()
        self.driver.find_element(By.ID, 'depositHomeLink').click()
        self.driver.find_element(By.ID, 'createCategoryLink').click()
        self.driver.find_element(By.NAME, 'name').send_keys('test')
        self.driver.find_element(By.ID, 'createCategoryButton').click()
        self.driver.find_element(By.ID, 'createDepositLink').click()
        category_dropdown = self.driver.find_element(By.NAME, 'category')
        category_select = Select(category_dropdown)
        category_select.select_by_index(1)
        self.driver.find_element(By.NAME, 'date').send_keys(datetime.now().strftime('%m-%d-%Y'))
        self.driver.find_element(By.NAME, 'description').send_keys('description')
        self.driver.find_element(By.NAME, 'amount').send_keys(-45.62)
        self.driver.find_element(By.ID, 'createDepositButton').click()
        self.assertEqual(self.driver.title, 'Create Deposit')

    ## Test create deposit feature success
    def test_create_deposit_feature_success(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginButton').click()
        self.driver.find_element(By.ID, 'trackFinancesButton').click()
        self.driver.find_element(By.ID, 'depositHomeLink').click()
        self.driver.find_element(By.ID, 'createCategoryLink').click()
        self.driver.find_element(By.NAME, 'name').send_keys('test')
        self.driver.find_element(By.ID, 'createCategoryButton').click()
        self.driver.find_element(By.ID, 'createDepositLink').click()
        category_dropdown = self.driver.find_element(By.NAME, 'category')
        category_select = Select(category_dropdown)
        category_select.select_by_index(1)
        self.driver.find_element(By.NAME, 'date').send_keys(datetime.now().strftime('%m-%d-%Y'))
        self.driver.find_element(By.NAME, 'description').send_keys('description')
        self.driver.find_element(By.NAME, 'amount').send_keys(45.62)
        self.driver.find_element(By.ID, 'createDepositButton').click()
        self.assertEqual(self.driver.title, 'Managing Deposits')
