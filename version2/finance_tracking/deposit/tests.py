from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
from datetime import datetime, timedelta
from .forms import DepositSearchForm
from django.urls import reverse
from ..models import *

# Test cases for deposit views
class TestDepositViews(TestCase):
    # Setup
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='password')
        self.category = Category.objects.create(name='Category 1', group=DEPOSIT, user=self.user)
        self.deposit =  Deposit.objects.create(amount=100, category=self.category, date=datetime.now(), user=self.user)
        
    ## Tests for home view
    # Test for home view redirect
    def test_home_view_redirect(self):
        response = self.client.get(reverse('deposit-home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)
        
    # Test home view rendering success
    def test_home_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('deposit-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/deposit/list.html')
        
    # Test home view search start only success
    def test_home_view_search_start_only_success(self):
        self.client.force_login(self.user)
        data = {
            'start_date': str(datetime.now().date()),
            'end_date': '',
            'deposit_id': ''
        }
        form = DepositSearchForm(data=data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('deposit-home'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/deposit/list.html')
                
    # Test home view exact search success
    def test_home_view_search_exact_success(self):
        self.client.force_login(self.user)
        data = {
            'start_date': '',
            'end_date': '',
            'deposit_id': self.deposit.id
        }
        form = DepositSearchForm(data=data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('deposit-home'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/deposit/list.html')

    # Test home view search success
    def test_home_view_search_search_success(self):
        self.client.force_login(self.user)
        data = {
            'start_date': str(datetime.now().date()),
            'end_date': str(datetime.now().date() - timedelta(days=30)),
            'deposit_id': ''
        }
        form = DepositSearchForm(data=data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('deposit-home'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/deposit/list.html')
   
    # Test home view pagination error
    def test_home_view_pagination_error(self):
        self.client.force_login(self.user)
        data = {
            'page': 'invalid_page_number'
        }
        response = self.client.get(reverse('deposit-home'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['deposits'].number, response.context['deposits'].paginator.num_pages)
        
    ## Tests for detail view
    # Test for detail view redirect
        
    # Test for detail view rendering success
        
    ## Tests for create view
    # Test for create view redirect
        
    # Test for create view rendering success
        
    # Test for create view success
        
    ## Tests for update view
    # Test for update view redirect
        
    # Test for update view rendering success
        
    # Test for update view success
        
    ## Tests for delete view
    # Test for delete view redirect
        
    # Test for delete view rendering success
        
    # Test for delete view success
        