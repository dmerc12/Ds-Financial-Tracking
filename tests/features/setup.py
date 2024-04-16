from main.finance_tracking.models import Category, Deposit, Expense
from django.contrib.auth.models import User
from main.users.models import CustomUser

# Function to setup test environment before selenium tests
def setup(self):
    self.base_user1 = User.objects.create_user(username='test1', first_name='first', last_name='last', email='first@last.com', password='pass12345')
    self.user1 = CustomUser.objects.create(user=self.base_user1, phone_number='1-111-222-3333')
    self.base_user2 = User.objects.create_user(username='test2', first_name='first', last_name='last', email='first@last.com', password='pass12345')
    self.user2 = CustomUser.objects.create(user=self.base_user2, phone_number='1-111-222-3333')
    self.base_user3 = User.objects.create_user(username='test3', first_name='first', last_name='last', email='first@last.com', password='pass12345')
    self.user3 = CustomUser.objects.create(user=self.base_user3, phone_number='1-111-222-3333')
    self.category1 = Category.objects.create(name='test1', user=self.base_user3, group='deposit')
    self.category2 = Category.objects.create(name='test2', user=self.base_user3, group='expense')
    self.category3 = Category.objects.create(name='test3', user=self.base_user3, group='deposit')
    self.category4 = Category.objects.create(name='test4', user=self.base_user3, group='expense')
    self.deposit1 = Deposit.objects.create(user=self.base_user3, category=self.category3, date='2024-01-12', description='test deposit 1', amount=45.35)
    self.expense1 = Expense.objects.create(user=self.base_user4, category=self.category3, date='2024-01-12', description='test expense 1', amount=45.35)
