from django.contrib.auth.models import User
from .forms import ChangePasswordForm
from django.test import TestCase

# Tests for the change password form
class TestChangePasswordFormT(TestCase):
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
