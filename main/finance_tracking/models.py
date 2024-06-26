from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Choices for categories
DEPOSIT = 'deposit'
EXPENSE = 'expense'

CATEGORY_CHOICES = {
    'deposit': DEPOSIT,
    'expense': EXPENSE
}

# Categories for deposits and expenses
class Category(models.Model):
    name = models.CharField(max_length=60)
    group = models.CharField(max_length=7, choices=CATEGORY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    # Overriding clean method
    def clean(self):
        if self.name.strip() == '':
            raise ValidationError('Name cannot be empty, please try again!')
        if len(self.name.strip()) > 60:
            raise ValidationError('Name cannot exceed 60 characters, please try again!')
        if self.group.strip() == '':
            raise ValidationError('Group cannot be empty, please try again!')

    # Overriding save method
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

# Deposits for income
class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(max_length=255)
    amount = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"Deposit - {self.pk}: user - {self.user.__str__()}, category - {self.category.__str__()}, date - {self.date}, description - {self.description}, amount - {self.amount}"

# Expenses for expenses and withdraws
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(max_length=255)
    amount = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"Expense - {self.pk}: user - {self.user.__str__()}, category - {self.category.__str__()}, date - {self.date}, description - {self.description}, amount - {self.amount}"
