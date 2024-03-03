from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
from datetime import datetime, timedelta
from django.urls import reverse
from ..models import *
from .forms import *

# Test cases for deposit views
class TestDepositViews(TestCase):
    # Setup
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='password')
        self.category = Category.objects.create(name='Category 1', group=DEPOSIT, user=self.user)
        self.deposit =  Deposit.objects.create(amount=100, category=self.category, date=datetime.now().date(), user=self.user)
        
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
        self.assertIsInstance(response.context['form'], DepositSearchForm)
        
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
        self.assertIsInstance(response.context['form'], DepositSearchForm)
                
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
        self.assertIsInstance(response.context['form'], DepositSearchForm)

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
        self.assertIsInstance(response.context['form'], DepositSearchForm)
   
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
    def test_detail_view_redirect(self):
        response = self.client.get(reverse('deposit-detail', args=[self.deposit.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)        

    # Test for detail view rendering success
    def test_detail_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('deposit-detail', args=[self.deposit.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/deposit/detail.html')

    # Test for detail view return url from view finances
    def test_deposit_detail_return_url_view_finances(self):
        self.client.force_login(self.user)
        url = reverse('deposit-detail', args=[self.deposit.id])
        response = self.client.get(url, HTTP_REFERER='/view/finances/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['return_url'], 'view-finances')
        
    ## Tests for create view
    # Test for create view redirect
    def test_create_view_redirect(self):
        response = self.client.get(reverse('create-deposit'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)        
        
    # Test for create view rendering success
    def test_create_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create-deposit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/deposit/create.html')
        self.assertIsInstance(response.context['form'], DepositForm)
        
    # Test for create view success
    def test_create_view_success(self):
        self.client.force_login(self.user)
        data = {
            'description': 'test description',
            'category': self.category.pk,
            'amount': 45.67,
            'date': datetime.now().date()
        }
        response = self.client.post(reverse('create-deposit'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('deposit-home'))
        self.assertTrue(Deposit.objects.filter(user=self.user, category=self.category, description=data['description'], amount=data['amount'], date=data['date']).exists())
        
    ## Tests for update view
    # Test for update view redirect
    def test_update_view_redirect(self):
        response = self.client.get(reverse('update-deposit', args=[self.deposit.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)        
        
    # Test for update view rendering success
    def test_update_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('update-deposit', args=[self.deposit.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/deposit/update.html')
        self.assertIsInstance(response.context['form'], DepositForm)
        
    # Test for update view success
    def test_update_view_success(self):
        self.client.force_login(self.user)
        data = {
            'description': 'updated description',
            'category': self.category.pk,
            'amount': 23.12,
            'date': datetime.now().date() - timedelta(days=34)
        }
        response = self.client.post(reverse('update-deposit', args=[self.deposit.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('deposit-home'))
        self.assertTrue(Deposit.objects.filter(user=self.deposit.user, pk=self.deposit.pk, category=self.deposit.category, description=data['description'], amount=data['amount'], date=data['date']).exists())
        
    ## Tests for delete view
    # Test for delete view redirect
        
    # Test for delete view rendering success
        
    # Test for delete view success
        