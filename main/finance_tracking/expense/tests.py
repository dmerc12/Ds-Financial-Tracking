from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
from datetime import datetime, timedelta
from django.urls import reverse
from ..models import *
from .forms import *

# Test cases for expense views
class TestExpenseViews(TestCase):
    # Setup
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='password')
        self.category = Category.objects.create(name='Category 1', group=EXPENSE, user=self.user)
        self.expense =  Expense.objects.create(amount=100, category=self.category, date=datetime.now().date(), user=self.user)
        
    ## Tests for home view
    # Test for home view redirect
    def test_home_view_redirect(self):
        response = self.client.get(reverse('expense-home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)
        
    # Test home view rendering success
    def test_home_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('expense-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/expense/list.html')
        self.assertIsInstance(response.context['form'], ExpenseSearchForm)
        
    # Test home view search start only success
    def test_home_view_search_start_only_success(self):
        self.client.force_login(self.user)
        data = {
            'start_date': str(datetime.now().date()),
            'end_date': '',
            'expense_id': ''
        }
        form = ExpenseSearchForm(data=data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('expense-home'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/expense/list.html')
        self.assertIsInstance(response.context['form'], ExpenseSearchForm)
                
    # Test home view exact search success
    def test_home_view_search_exact_success(self):
        self.client.force_login(self.user)
        data = {
            'start_date': '',
            'end_date': '',
            'expense_id': self.expense.pk
        }
        form = ExpenseSearchForm(data=data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('expense-home'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/expense/list.html')
        self.assertIsInstance(response.context['form'], ExpenseSearchForm)

    # Test home view search success
    def test_home_view_search_search_success(self):
        self.client.force_login(self.user)
        data = {
            'start_date': str(datetime.now().date()),
            'end_date': str(datetime.now().date() - timedelta(days=30)),
            'expense_id': ''
        }
        form = ExpenseSearchForm(data=data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('expense-home'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/expense/list.html')
        self.assertIsInstance(response.context['form'], ExpenseSearchForm)
   
    # Test home view pagination error
    def test_home_view_pagination_error(self):
        self.client.force_login(self.user)
        data = {
            'page': 'invalid_page_number'
        }
        response = self.client.get(reverse('expense-home'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['expenses'].number, response.context['expenses'].paginator.num_pages)
        
    ## Tests for detail view
    # Test for detail view redirect
    def test_detail_view_redirect(self):
        response = self.client.get(reverse('expense-detail', args=[self.expense.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)        

    # Test for detail view rendering success
    def test_detail_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('expense-detail', args=[self.expense.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/expense/detail.html')

    # Test for detail view return url from view finances
    def test_detail_return_url_view_finances(self):
        self.client.force_login(self.user)
        url = reverse('expense-detail', args=[self.expense.pk])
        response = self.client.get(url, HTTP_REFERER='/view/finances/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['return_url'], 'view-finances')
        
    ## Tests for create view
    # Test for create view redirect
    def test_create_view_redirect(self):
        response = self.client.get(reverse('create-expense'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)        
        
    # Test for create view rendering success
    def test_create_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create-expense'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/expense/create.html')
        self.assertIsInstance(response.context['form'], ExpenseForm)
        
    # Test for create view success
    def test_create_view_success(self):
        self.client.force_login(self.user)
        data = {
            'description': 'test description',
            'category': self.category.pk,
            'amount': 45.67,
            'date': datetime.now().date()
        }
        response = self.client.post(reverse('create-expense'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('expense-home'))
        self.assertTrue(Expense.objects.filter(user=self.user, category=self.category, description=data['description'], amount=data['amount'], date=data['date']).exists())
        
    ## Tests for update view
    # Test for update view redirect
    def test_update_view_redirect(self):
        response = self.client.get(reverse('update-expense', args=[self.expense.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)        
        
    # Test for update view rendering success
    def test_update_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('update-expense', args=[self.expense.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/expense/update.html')
        self.assertIsInstance(response.context['form'], ExpenseForm)
        
    # Test for update view success
    def test_update_view_success(self):
        self.client.force_login(self.user)
        data = {
            'description': 'updated description',
            'category': self.category.pk,
            'amount': 23.12,
            'date': datetime.now().date() - timedelta(days=34)
        }
        response = self.client.post(reverse('update-expense', args=[self.expense.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('expense-home'))
        self.assertTrue(Expense.objects.filter(user=self.expense.user, pk=self.expense.pk, category=self.expense.category, description=data['description'], amount=data['amount'], date=data['date']).exists())
        
    ## Tests for delete view
    # Test for delete view redirect
    def test_delete_view_redirect(self):
        response = self.client.get(reverse('delete-expense', args=[self.expense.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)        
        
    # Test for delete view rendering success
    def test_delete_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('delete-expense', args=[self.expense.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/expense/delete.html')
        
    # Test for delete view success
    def test_delete_view_success(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('delete-expense', args=[self.expense.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('expense-home'))
        self.assertFalse(Expense.objects.filter(pk=self.expense.pk).exists())
       