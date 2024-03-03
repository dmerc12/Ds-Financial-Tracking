from django.core.exceptions import ValidationError
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
from datetime import datetime, timedelta
from django.utils import timezone
from django.urls import reverse
from .forms import SearchForm
from .models import *

# Test cases for finance tracking models
class TestFinanceTrackingModels(TestCase):

    # Setup
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password')
        self.deposit_category = Category.objects.create(name='Category 1', group=DEPOSIT, user=self.user)
        self.expense_category = Category.objects.create(name='Category 2', group=EXPENSE, user=self.user)
        self.deposit =  Deposit.objects.create(amount=100, category=self.deposit_category, date=datetime.now(), user=self.user)
        self.expense =  Expense.objects.create(amount=100, category=self.expense_category, date=datetime.now(), user=self.user)
        
    ## Tests for category model
    # Test for category string method
    def test_category_string_method(self):
        category_str = str(self.deposit_category)
        self.assertEqual(category_str, self.deposit_category.name)
        
    # Test for category name empty
    def test_category_name_empty(self):
        with self.assertRaises(ValidationError) as context:
            Category.objects.create(name='', group=DEPOSIT, user=self.user)
        self.assertTrue('Name cannot be empty, please try again!' in str(context.exception))

    # Test for category group empty
    def test_category_group_empty(self):
        with self.assertRaises(ValidationError) as context:
            Category.objects.create(name='Test', group='', user=self.user)
        self.assertTrue('Group cannot be empty, please try again!' in str(context.exception))

    ## Tests for deposit model
    # Test for deposit string method
    def test_deposit_string_method(self):
        deposit_str = str(self.deposit)
        self.assertEqual(deposit_str, f'Deposit - {self.deposit.pk}: user - {self.deposit.user.__str__()}, category - {self.deposit.category.__str__()}, date - {self.deposit.date}, description - {self.deposit.description}, amount - {self.deposit.amount}')
        
    ## Tests for expense model
    # Test for expense string method
    def test_expense_string_method(self):
        expense_str = str(self.expense)
        self.assertEqual(expense_str, f'Expense - {self.expense.pk}: user - {self.expense.user.__str__()}, category - {self.expense.category.__str__()}, date - {self.expense.date}, description - {self.expense.description}, amount - {self.expense.amount}')
        
# Test cases for finance tracking views
class TestFinanceTrackingViews(TestCase):

    # Setup
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='password')

    ## Tests for home view
    # Test for home view redirect
    def test_home_view_redirect(self):
        response = self.client.get(reverse('finance-home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)
        
    # Test for home view rendering success
    def test_home_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('finance-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/home.html')
        
    ## Tests for view finances view
    # Test for view finances view redirect
    def test_view_finances_view_redirect(self):
        response = self.client.get(reverse('view-finances'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)
        
    # Test for view finances view rendering success
    def test_view_finances_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('view-finances'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/view_finances.html')
        
    # Test for view finances view search success
    def test_view_finances_view_search_success(self):
        self.client.force_login(self.user)
        start_date = str(datetime.now().date() - timedelta(weeks=1))
        end_date = str(datetime.now().date())
        data = {
            'start_date': start_date,
            'end_date': end_date
        }
        form = SearchForm(data=data)
        self.assertTrue(form.is_valid())
        response = self.client.get(reverse('view-finances'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/view_finances.html')

    # Test for view finances view pagination error
    def test_view_finances_view_pagination(self):
        self.client.force_login(self.user)
        data = {
            'page': 'invalid_page_number'
        }
        response = self.client.get(reverse('view-finances'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['transactions'].number, response.context['transactions'].paginator.num_pages)
            
    ## Tests for analyze finances view
    # Test for analyze finances view redirect
    def test_analyze_finances_view_redirect(self):
        response = self.client.get(reverse('analyze-finances'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test for analyze finances view rendering success
    def test_analyze_finances_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('analyze-finances'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/analyze_finances.html')
        
    # Test for analyze finances view search success
    def test_analyze_finances_view_search_success(self):
        self.client.force_login(self.user)
        data = {
            'start_date': datetime.now().date() - timedelta(weeks=1),
            'end_date': datetime.now().date() - timedelta(weeks=4)
        }
        form = SearchForm(data=data)
        self.assertTrue(form.is_valid())
        response = self.client.get(reverse('analyze-finances'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/analyze_finances.html')
