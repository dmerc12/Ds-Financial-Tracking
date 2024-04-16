from main.finance_tracking.models import Category, Deposit, Expense
from django.core.management import call_command
from django.contrib.auth.models import User
from main.users.models import CustomUser

# Function to cleanup test environment after selenium tests
def cleanup():
    ## Delete all objects
    User.objects.all().delete()
    CustomUser.objects.all().delete()
    Category.objects.all().delete()
    Deposit.objects.all().delete()
    Expense.objects.all().delete()

    ## Reset ID sequence for each model
    call_command('sqlsequencereset', 'auth', 'users', 'main_users_customuser', 'main_finance_tracking_category', 'main_finance_tracking_deposit', 'main_finance_tracking_expense', interactive=False)
