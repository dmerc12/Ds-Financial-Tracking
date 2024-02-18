from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='password')

    def test_home_view_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/')

    def test_home_view_returns_home_template_if_logged_in(self):
        self.client.login(username='test_user', password='password')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'entry/home.html')
