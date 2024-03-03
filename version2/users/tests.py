from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.contrib.auth import get_user
from django.urls import reverse
from .models import *
from .forms import *

# Tests for user model
class TestUserModel(TestCase):

    # Setup before tests
    def setUp(self):
        self.base_user = User.objects.create(first_name='first', last_name='last', username='firstlast', password='testuser', email='testuser@example.com')
        self.user = CustomUser.objects.create(phone_number='1-234-567-8901', user=self.base_user)

    # Test string method
    def test_string_method(self):
        user_str = str(self.user)
        expected_str = f'{self.user.user.first_name} {self.user.user.last_name}'
        self.assertEqual(user_str, expected_str)

    # Test first_name method
    def test_first_name_method(self):
        first_name = self.user.first_name()
        self.assertEqual(first_name, self.user.user.first_name)

    # Test last_name method
    def test_last_name_method(self):
        last_name = self.user.last_name()
        self.assertEqual(last_name, self.user.user.last_name)

    # Test email method
    def test_email_method(self):
        email = self.user.email()
        self.assertEqual(email, self.user.user.email)

    # Test username method
    def test_username_method(self):
        username = self.user.username()
        self.assertEqual(username, self.user.user.username)

# Tests for user forms
class TestUserForms(TestCase):

    # Setup before tests
    def setUp(self):
        self.base_user = User.objects.create(first_name='first', last_name='last', username='firstlast', password='testuser', email='testuser@example.com')
        self.user = CustomUser.objects.create(phone_number='1-234-567-8901', user=self.base_user)
    
    ## Tests for register form
    # Test for form initializaion
    def test_register_form_initializaton(self):
        form = RegisterForm()
        self.assertIn('username', form.fields.keys())
        self.assertIn('first_name', form.fields.keys())
        self.assertIn('last_name', form.fields.keys())
        self.assertIn('email', form.fields.keys())
        self.assertIn('phone_number', form.fields.keys())
        self.assertIn('password1', form.fields.keys())
        self.assertIn('password2', form.fields.keys())

    # Test for form validation with empty fields
    def test_register_form_validation_empty_fields(self):
        data = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone_number': '',
            'password1': '',
            'password2': ''
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)

    # Test for form validation with fields too long
    def test_register_form_validation_fields_too_long(self):
        data = {
            'username': 'this is too long and so the validation will fail and then the test will pass and be successful so for once I\'m hoping that the test fails so it checks my validation logic correctly',
            'first_name': 'this is too long and so the validation will fail and then the test will pass and be successful so for once I\'m hoping that the test fails so it checks my validation logic correctly',
            'last_name': 'this is too long and so the validation will fail and then the test will pass and be successful so for once I\'m hoping that the test fails so it checks my validation logic correctly',
            'email': 'thisistoolongandsothevalidationwillfailandthenthetestwillpassandbesuccessfulsoforonceI\'mhopingthatthetestfailssoitchecksmyvalidationlogiccorrectlysopleasefailsothistestwillpassandIwillbesohappy@email.com',
            'phone_number': 'this is too long and so the validation will fail and then the test will pass and be successful so for once I\'m hoping that the test fails so it checks my validation logic correctly',
            'password1': 'this is too long and so the validation will fail and then the test will pass and be successful so for once I\'m hoping that the test fails so it checks my validation logic correctly',
            'password2': 'this is too long and so the validation will fail and then the test will pass and be successful so for once I\'m hoping that the test fails so it checks my validation logic correctly'
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)

    # Test for form validation with invalid email
    def test_register_form_validation_invalid_email(self):
        data = {
            'username': 'username',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'test user email',
            'phone_number': '1-234-234-2917',
            'password1': 'this will pass',
            'password2': 'this will pass'
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    # Test for form validation with mismatching passwords
    def test_register_form_validation_mismatching_passwords(self):
        data = {
            'username': 'username',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'testuser@example.com',
            'phone_number': '1-234-234-2917',
            'password1': 'nope',
            'password2': 'this will not pass'
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    # Test for form validation with invalid password
    def test_register_form_validation_invalid_password(self):
        data = {
            'username': 'username',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'testuser@example.com',
            'phone_number': '1-234-234-2917',
            'password1': 'username',
            'password2': 'username'
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    # Test for form validation success
    def test_register_form_validation_success(self):
        data = {
            'username': 'username',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'testuser@example.com',
            'phone_number': '1-234-234-2917',
            'password1': 'this will pass',
            'password2': 'this will pass'
        }
        form = RegisterForm(data=data)
        self.assertTrue(form.is_valid())

    ## Tests for update user form
    # Test for form initializaion
    def test_update_user_form_initializaton(self):
        form = UpdateUserForm()
        self.assertIn('username', form.fields.keys())
        self.assertIn('first_name', form.fields.keys())
        self.assertIn('last_name', form.fields.keys())
        self.assertIn('email', form.fields.keys())
        self.assertIn('phone_number', form.fields.keys())

    # Test for form validation with empty fields
    def test_update_user_form_validation_empty_fields(self):
        data = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone_number': '',
        }
        form = UpdateUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)

    # Test for form validation with fields too long
    def test_update_user_form_validation_fields_too_long(self):
        data = {
            'username': 'this is too long and so the validation will fail and then the test will pass and be successful so for once I\'m hoping that the test fails so it checks my validation logic correctly',
            'first_name': 'this is too long and so the validation will fail and then the test will pass and be successful so for once I\'m hoping that the test fails so it checks my validation logic correctly',
            'last_name': 'this is too long and so the validation will fail and then the test will pass and be successful so for once I\'m hoping that the test fails so it checks my validation logic correctly',
            'email': 'thisistoolongandsothevalidationwillfailandthenthetestwillpassandbesuccessfulsoforonceI\'mhopingthatthetestfailssoitchecksmyvalidationlogiccorrectlysopleasefailsothistestwillpassandIwillbesohappy@email.com',
            'phone_number': 'this is too long and so the validation will fail and then the test will pass and be successful so for once I\'m hoping that the test fails so it checks my validation logic correctly',
        }
        form = UpdateUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)

    # Test for form validation with invalid email
    def test_update_user_form_validation_invalid_email(self):
        data = {
            'username': 'username',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'test user email',
            'phone_number': '1-234-234-2917',
        }
        form = UpdateUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    # Test for form validation success
    def test_update_user_form_validation_success(self):
        data = {
            'username': 'updated',
            'first_name': 'updated',
            'last_name': 'updated',
            'email': 'updated@email.com',
            'phone_number': '91-999-237-4456',
        }
        form = UpdateUserForm(data=data)
        self.assertTrue(form.is_valid())

    ## Tests for change password form
    # Test for form initializaion
    def test_change_password_form_initializaton(self):
        form = ChangePasswordForm(user=self.user)
        self.assertIn('new_password1', form.fields.keys())
        self.assertIn('new_password2', form.fields.keys())

    # Test for form validation with empty fields
    def test_change_password_form_validation_empty_fields(self):
        data = {
            'new_password1': '',
            'new_password2': ''
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password1', form.errors)
        self.assertIn('new_password2', form.errors)

    # Test for form validation with mismatching passwords
    def test_change_password_form_validation_mismatching_passwords(self):
        data = {
            'new_password1': 'nope',
            'new_password2': 'this will not pass'
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

    # Test for form validation with invalid password
    def test_change_password_form_validation_invalid_password(self):
        data = {
            'new_password1': 'updated',
            'new_password2': 'updated'
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

    # Test for form validation success
    def test_change_password_form_validation_success(self):
        data = {
            'new_password1': 'new_password',
            'new_password2': 'new_password'
        }
        form = ChangePasswordForm(user=self.user, data=data)
        self.assertTrue(form.is_valid())

# Tests for user views
class TestUserViews(TestCase):
    
    # Setup before tests
    def setUp(self):
        self.base_user = User.objects.create_user(first_name='first', last_name='last', username='firstlast', password='testuser', email='testuser@example.com')
        self.user = CustomUser.objects.create(phone_number='1-234-567-8901', user=self.base_user)

    ## Tests for login view
    # Test for login view rendering success
    def test_login_view_rendering_success(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    # Test for login view with empty fields
    def test_login_view_empty_fields(self):
        data = {
            'username': '',
            'password': ''
        }
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Incorrect username or password, please try again!', messages)

    # Test for login view with incorrect credentials
    def test_login_view_incorrect_credentials(self):
        data = {
            'username': 'firstlast',
            'password': 'incorrect'
        }
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Incorrect username or password, please try again!', messages)

    # Test for login view success
    def test_login_view_success(self):
        data = {
            'username': 'firstlast',
            'password': 'testuser'
        }
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        user = get_user(response.wsgi_request)
        self.assertTrue(user.is_authenticated)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(f'Welcome {self.user.user.first_name}!', messages)

    ## Tests for logout view
    # Test for logout view success
    def test_logout_view_success(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Goodbye!', messages)
        
    ## Tests for register view
    # Test for register view rendering success
    def test_register_view_rendering_success(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
        self.assertIsInstance(response.context['form'], RegisterForm)
        
    # Test for register view success
    def test_register_view_success(self):
        data = {
            'username': 'username',
            'first_name': 'user',
            'last_name': 'name',
            'email': 'test@example.com',
            'phone_number': '1-234-232-3495',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        }
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(CustomUser.objects.filter(user__username=data['username'], user__first_name=data['first_name'], user__last_name=data['last_name'], user__email=data['email'], phone_number=data['phone_number']).exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You have been successfully registered! Welcome!', messages)
        
    ## Tests for update user view
    # Test for update user view when not logged in
    def test_update_user_view_not_logged_in(self):
        response = self.client.get(reverse('update-user'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)
        
    # Test for update user view rendering success
    def test_update_user_view_rendering_success(self):
        self.client.force_login(self.user.user)
        response = self.client.get(reverse('update-user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/update.html')
        self.assertIsInstance(response.context['form'], UpdateUserForm)
        
    # Test for update user view success
    def test_update_user_view_success(self):
        data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'phone_number': '99-154-879-6749',
            'first_name': 'updated',
            'last_name': 'user'
        }
        self.client.force_login(self.user.user)
        response = self.client.post(reverse('update-user'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(CustomUser.objects.filter(user__username=data['username'], user__first_name=data['first_name'], user__last_name=data['last_name'], user__email=data['email'], phone_number=data['phone_number']).exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Your profile has been successfully updated!', messages)
        
    ## Tests for change password view
    # Test for change password view when not logged in
    def test_change_password_view_not_logged_in(self):
        response = self.client.get(reverse('change-password'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test for change password view rendering success
    def test_change_password_view_rendering_success(self):
        self.client.force_login(self.user.user)
        response = self.client.get(reverse('change-password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/change_password.html')
        self.assertIsInstance(response.context['form'], ChangePasswordForm)

    # Test for change password view success
    def test_change_password_success(self):
        data = {
            'new_password1': 'updatedpassword123',
            'new_password2': 'updatedpassword123'
        }
        self.client.force_login(self.user.user)
        response = self.client.post(reverse('change-password'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Your password has been changed!', messages)
        
    ## Tests for delete user view
    # Test for delete user view when not logged in
    def test_delete_user_not_logged_in(self):
        response = self.client.get(reverse('delete-user'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('You must be logged in to access this page. Please register or login then try again!', messages)

    # Test for delete user rendering success
    def test_delete_user_rendering_success(self):
        self.client.force_login(self.user.user)
        response = self.client.get(reverse('delete-user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/delete.html')

    # Test for delete user success
    def test_delete_user_success(self):
        self.client.force_login(self.user.user)
        response = self.client.post(reverse('delete-user'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertFalse(CustomUser.objects.filter(pk=self.user.pk).exists())
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('Your profile has been successfully deleted, goodbye!', messages)
        