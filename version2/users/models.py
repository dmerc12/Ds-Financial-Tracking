from django.contrib.auth.models import User
from django.db import models

# Users
class CustomUser(models.Model):
    phone_number = models.CharField(max_length=20, help_text='Please enter a valid phone number.')
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def first_name(self):
        return self.user.first_name
    
    def last_name(self):
        return self.user.last_name
    
    def email(self):
        return self.user.email
    
    def username(self):
        return self.user.username
    