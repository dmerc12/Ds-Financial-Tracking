from selenium.webdriver.edge.webdriver import WebDriver
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from datetime import datetime, timedelta
from users.models import CustomUser
from tests.other.POMs import search

# Tests for search feature
class SearchTests(LiveServerTestCase):

    def setUp(self):
        ### Setup test data
        self.password = 'pass12345'
        self.user = User.objects.create_user(username='test1', password=self.password, first_name='first', last_name='last', email='test1@email.com')
        self.profile = CustomUser.objects.create(user=self.user, phone_number='1-222-333-4444')

        ### Setup webdriver
        self.driver = WebDriver()

    def test_search_analyze_finances(self):
        search.search_analyze_finances(self, 'Analyzing Finances', self.user.username, self.password, (datetime.now().date() - timedelta(days=45)).strftime('%m-%d-%Y'), datetime.now().date().strftime('%m-%d-%Y'))
