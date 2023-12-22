from django.db import models
from ..users.models import User

class Category(models.Model):
    name = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=7)
