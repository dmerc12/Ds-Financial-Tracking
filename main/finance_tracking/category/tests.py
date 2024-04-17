from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from ..models import *

# Test cases for category views
class TestCategoryViews(TestCase):
    # Setup
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='password')
        self.category1 = Category.objects.create(name='Category 1', group=DEPOSIT, user=self.user)
        self.category2 = Category.objects.create(name='Category 2', group=DEPOSIT, user=self.user)
        self.deposit =  Deposit.objects.create(amount=100, category=self.category2, date=datetime.now(), user=self.user)

    ## Tests for create category view
    # Test create category view redirects if user not logged in
    def test_create_category_view_redirect(self):
        response = self.client.get(reverse('create-category', args=['deposit']))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test create category view returns correct template
    def test_create_category_view_rendering_success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create-category', args=['deposit']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/category/create.html')

    # Test create category view success
    def test_create_category_view_success(self):
        self.client.login(username='test_user', password='password')
        data = {'name': 'Testing 123', 'group': 'deposit'}
        response = self.client.post(reverse('create-category', args=['deposit']), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name='Testing 123', group='deposit', user=self.user).exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Category successfully created!', messages)

    ## Tests for update category view
    # Test update category view redirects if user not logged in
    def test_update_category_view_redirect(self):
        self.client.logout()
        response = self.client.get(reverse('update-category', args=[self.category1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test update category view returns correct template
    def test_update_category_view_rendering_success(self):
        self.client.login(username='test_user', password='password')
        response = self.client.get(reverse('update-category', args=[self.category1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/category/update.html')

    # Test update category view success
    def test_update_category_view_success(self):
        self.client.login(username='test_user', password='password')
        data = {'name': 'Updated Category', 'group': DEPOSIT}
        response = self.client.post(reverse('update-category', args=[self.category1.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name='Updated Category', group=DEPOSIT, user=self.user).exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Category successfully updated!', messages)

    ## Tests for delete category view
    # Test delete category view redirects if user not logged in
    def test_delete_category_view_redirect(self):
        self.client.logout()
        response = self.client.get(reverse('delete-category', args=[self.category1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test delete category view returns correct template
    def test_delete_category_view_rendering_success(self):
        self.client.login(username='test_user', password='password')
        response = self.client.get(reverse('delete-category', args=[self.category1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/category/delete.html')

    # Test delete category view success
    def test_delete_category_view_success(self):
        deposits_to_delete = Deposit.objects.filter(category=self.category1)
        deposits_to_delete.delete()
        self.client.login(username='test_user', password='password')
        response = self.client.post(reverse('delete-category', args=[self.category1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Category.objects.filter(name='Category 1', group=DEPOSIT, user=self.user).exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Category successfully deleted!', messages)

    # Test delete category when used by an expense or deposit
    def test_delete_category_view_category_in_use(self):
        self.client.login(username='test_user', password='password')
        response = self.client.post(reverse('delete-category', args=[self.category2.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name='Category 2', group=DEPOSIT, user=self.user).exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Category is currently being used and cannot be deleted!', messages)
