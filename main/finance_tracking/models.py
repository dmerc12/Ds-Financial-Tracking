from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=60)
    group = models.CharField(max_length=7)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(max_length=255)
    amount = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"Deposit - {self.pk}: user - {self.user.__str__()}, category - {self.category.__str__()}, date - {self.date}, description - {self.description}, amount - {self.amount}"

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=255)
    amount = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"Expense - {self.pk}: user - {self.user.__str__()}, category - {self.category.__str__()}, date - {self.date}, description - {self.description}, amount - {self.amount}"
