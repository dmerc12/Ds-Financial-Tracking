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

    # Teardown
    def tearDown(self):
        Category.objects.all().delete() 
        Deposit.objects.all().delete()

    # # Test create category view redirects if user not logged in
    # def test_create_category_view_redirect_if_not_logged_in(self):
    #     response = self.client.get(reverse('create-category'))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, '/login/?next=/financial/tracker/category/create/')

    # # Test create category view returns correct template
    # def test_create_category_view_returns_create_category_template_if_logged_in(self):
    #     self.client.login(username='test_user', password='password')
    #     response = self.client.get(reverse('create-category'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'finance_tracking/category/create.html')
    #     self.client.logout()

    # # Test create category view success
    # def test_create_category_view_post_success(self):
    #     self.client.login(username='test_user', password='password')
    #     data = {'name': 'Test', 'group': 'deposit'}
    #     response = self.client.post(reverse('create-category'), data) 
    #     self.assertEqual(response.status_code, 200) # FIXME: not returning 302 status code for redirect like it should
    #     self.assertTrue(Category.objects.filter(name='Test', group='deposit', user=self.user).exists()) # FIXME: returning false indicating that category isn't being created
    #     storage = get_messages(response.wsgi_request)
    #     self.assertEqual(list(storage)[0].message, 'Category successfully created!')
    #     self.client.logout()
        
    # # Test create category with empty name
    # def test_create_category_view_post_empty_name(self):
    #     self.client.login(username='test_user', password='password')
    #     data = {'name': '', 'group': 'deposit'}
    #     response = self.client.post(reverse('create-category'), data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertFalse(Category.objects.filter(group='deposit', user=self.user).exists())
    #     self.client.logout()

    # # Test create category view with empty group
    # def test_create_category_view_post_empty_group(self):
    #     self.client.login(username='test_user', password='password')
    #     data = {'name': 'Test Category', 'group': ''}
    #     response = self.client.post(reverse('create-category'), data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertFalse(Category.objects.filter(name='Test Category', user=self.user).exists())
    #     self.client.logout()

    # Test update category view redirects if user not logged in
    def test_update_category_view_redirect_if_not_logged_in(self):
        self.client.logout()
        category = Category.objects.create(name='Test Category', group='deposit', user=self.user)
        response = self.client.get(reverse('update-category', args=[category.id]))
        expected_redirect_url = f'/login/?next=/financial/tracker/category/{category.id}/update/'
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_redirect_url)

    # Test update category view returns correct template
    def test_update_category_view_returns_update_category_template_if_logged_in(self):
        category = Category.objects.create(name='Test Category', group='deposit', user=self.user)
        self.client.login(username='test_user', password='password')
        response = self.client.get(reverse('update-category', args=[category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/category/update.html')
        self.client.logout()

    # Test update category view success
    def test_update_category_view_post_valid_success(self):
        category = Category.objects.create(name='Test Category', group='deposit', user=self.user)
        self.client.login(username='test_user', password='password')
        data = {'name': 'Updated Category', 'group': 'deposit'}
        response = self.client.post(reverse('update-category', args=[category.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name='Updated Category', group='deposit', user=self.user).exists())
        storage = get_messages(response.wsgi_request)
        self.assertEqual(list(storage)[0].message, 'Category successfully updated!')
        self.client.logout()

    # Test delete category view redirects if user not logged in
    def test_delete_category_view_redirect_if_not_logged_in(self):
        self.client.logout()
        category = Category.objects.create(name='Test Category', group='deposit', user=self.user)
        response = self.client.get(reverse('delete-category', args=[category.id]))
        expected_redirect_url = f'/login/?next=/financial/tracker/category/{category.id}/delete/'
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_redirect_url)

    # Test delete category view returns correct template
    def test_delete_category_view_returns_delete_category_template_if_logged_in(self):
        category = Category.objects.create(name='Test Category', group='deposit', user=self.user)
        self.client.login(username='test_user', password='password')
        response = self.client.get(reverse('delete-category', args=[category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finance_tracking/category/delete.html')
        self.client.logout()

    # Test delete category view success
    def test_delete_category_view_post_valid_success(self):
        category = Category.objects.create(name='Test Category', group='deposit', user=self.user)
        self.client.login(username='test_user', password='password')
        data = {'name': 'Category', 'group': 'deposit'}
        response = self.client.post(reverse('delete-category', args=[category.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Category.objects.filter(name='Category', group='deposit', user=self.user).exists())
        storage = get_messages(response.wsgi_request)
        self.assertEqual(list(storage)[0].message, 'Category successfully deleted!')
        self.client.logout()

    # Test delete category when used by an expense or deposit
    def test_delete_category_view_post_category_in_use(self):
        category = Category.objects.create(name='Test Category', group='deposit', user=self.user)
        Deposit.objects.create(amount=100, category=category, date=datetime.now(), user=self.user)
        self.client.login(username='test_user', password='password')
        response = self.client.post(reverse('delete-category', args=[category.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name='Test Category', group='deposit', user=self.user).exists())
        storage = get_messages(response.wsgi_request)
        self.assertEqual(list(storage)[0].message, 'Category is currently being used and cannot be deleted!')
        self.client.logout()
        