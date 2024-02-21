from django.contrib.auth.models import User
from django.test import TestCase, Client
from .forms import ChangePasswordForm
from django.urls import reverse

# Tests for the change password form
class TestChangePasswordForm(TestCase):
    # Setup before the tests
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='old_password')

    # Test that the password is being initialized correctly
    def test_form_initialization(self):
        form = ChangePasswordForm(user=self.user)
        self.assertNotIn('old_password', form.fields.keys())

    # Tests form validation
    def test_form_validation(self):
        # Test passwords not matching
        data = {
            'new_password1': 'new_password',
            'new_password2': 'not_matching_password'
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

    # Test home view redirects if user not logged in
    def test_home_view_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('user-home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/users/')

    # Test home view
    def test_home_view(self):
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
