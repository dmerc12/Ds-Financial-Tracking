from django.core.exceptions import ValidationError
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from .models import *

# Test cases for finance tracking models
class TestFinanceTrackingModels(TestCase):

    # Setup
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password')
        self.deposit_category = Category.objects.create(name='Category 1', group=DEPOSIT, user=self.user)
        self.expense_category = Category.objects.create(name='Category 2', group=EXPENSE, user=self.user)
        self.deposit =  Deposit.objects.create(amount=100, category=self.deposit_category, date=datetime.now(), user=self.user)
        self.expense =  Expense.objects.create(amount=100, category=self.expense_category, date=datetime.now(), user=self.user)
        
    ## Tests for category model
    # Test for category string method
    def test_category_string_method(self):
        category_str = str(self.deposit_category)
        self.assertEqual(category_str, self.deposit_category.name)
        
    # Test for category name empty
    def test_category_name_empty(self):
        with self.assertRaises(ValidationError) as context:
            Category.objects.create(name='', group=DEPOSIT, user=self.user)
        self.assertTrue('Name cannot be empty, please try again!' in str(context.exception))

    # Test for category group empty
    def test_category_group_empty(self):
        with self.assertRaises(ValidationError) as context:
            Category.objects.create(name='Test', group='', user=self.user)
        self.assertTrue('Group cannot be empty, please try again!' in str(context.exception))

    ## Tests for deposit model
    # Test for deposit string method
    def test_deposit_string_method(self):
        deposit_str = str(self.deposit)
        self.assertEqual(deposit_str, f'Deposit - {self.deposit.pk}: user - {self.deposit.user.__str__()}, category - {self.deposit.category.__str__()}, date - {self.deposit.date}, description - {self.deposit.description}, amount - {self.deposit.amount}')
        
    ## Tests for expense model
    # Test for expense string method
    def test_expense_string_method(self):
        expense_str = str(self.expense)
        self.assertEqual(expense_str, f'Expense - {self.expense.pk}: user - {self.expense.user.__str__()}, category - {self.expense.category.__str__()}, date - {self.expense.date}, description - {self.expense.description}, amount - {self.expense.amount}')
        
# Test cases for finance tracking views
class TestFinanceTrackingViews(TestCase):

    # Setup
    def setUp(self):
        self.client = Client()

    