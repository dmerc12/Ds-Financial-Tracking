from django.contrib.auth.models import User
from django.test import TestCase, Client
from .forms import ChangePasswordForm
from django.urls import reverse

# Tests for the change password form
class TestChangePasswordForm(TestCase):
    # Setup before the tests
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='old_password', first_name='test', last_name='user', email='testuser@example.com') 

    # Tests form initialization validation
    def test_form_initialization_and_validation(self):
        # Test form initialization
        form = ChangePasswordForm(user=self.user)
        self.assertNotIn('old_password', form.fields.keys())

        ## Test form validation

        # Test passwords not matching
        data = {
            'new_password1': 'new_password',
            'new_password2': 'not_matching_password'
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

        # Test empty passwords
        data = {
            'new_password1': '',
            'new_password2': ''
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

        # Test passwords contain username
        data = {
            'new_password1': 'testuser',
            'new_password2': 'testuser'
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

        # Test passwords contain first name
        data = {
            'new_password1': 'test',
            'new_password2': 'test'
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

        # Test passwords contain last name
        data = {
            'new_password1': 'user',
            'new_password2': 'user'
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

        # Test passwords contain email address
        data = {
            'new_password1': 'testuser@email.com',
            'new_password2': 'testuser@email.com'
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

        # Test success
        data['new_password2'] = 'new_password'
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertTrue(form.is_valid)

# Tests for the user views
class TestUserView(TestCase):
    # Setup before the tests
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='old_password')

    # Teardown after tests
    def tearDown(self):
        User.objects.all().delete() 

    # Test home view
    def test_home_view(self):
        # Test view redirects if user not logged in
        response = self.client.get(reverse('user-home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/users/')

        # Test view with user logged in
        self.client.force_login(self.user)
        response = self.client.get(reverse('user-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/home.html')

    # Test register view
    def test_register_view(self):
        # Test rendering correct template when going to page
        response = self.client.get(reverse('add-user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

        # Test success
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(reverse('add-user'), data)
        self.assertEqual(response.status_code, 302)

    # Test update user view
    def test_update_view(self):
        # Test view redirects if user not logged in
        response = self.client.get(reverse('update-user'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/users/update/')

        # Test view with user logged in
        self.client.force_login(self.user)

        # Test rendering correct template when going to page
        response = self.client.get(reverse('update-user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/update.html')

        # Test success
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(reverse('update-user'), data)
        self.assertEqual(response.status_code, 302)
