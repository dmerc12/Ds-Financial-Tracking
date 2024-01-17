from django.contrib import admin
from .models import Category, Deposit, Expense

admin.site.register(Category)
admin.site.register(Deposit)
admin.site.register(Expense)
