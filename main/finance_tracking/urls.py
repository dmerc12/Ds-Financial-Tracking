from . import views
from django.urls import path
from django.contrib import admin
from .category import views as category_views
from .deposit import views as deposit_views
# from .expense import views as expense_views

urlpatterns = [
    # path('', views.home, name='finance-tracking-home'),
    path('category/create/', category_views.create_category, name='create-category'),
    path('category/<int:category_id>/update/', category_views.update_category, name='update-category'),
    path('category/<int:category_id>/delete/', category_views.delete_category, name='delete-category'),
    path('deposits/', deposit_views.home, name='deposit-home'),
    path('deposits/year/', deposit_views.home_by_year, name='deposit-home-by-year'),
    path('deposits/category/', deposit_views.home_by_category, name='deposit-home-by-category'),    
    path('deposit/<int:deposit_id>/', deposit_views.deposit_detail, name='deposit-detail'),
    path('deposit/create/', deposit_views.create_deposit, name='create-deposit'),
    path('deposit/<int:deposit_id>/update/', deposit_views.update_deposit, name='update-deposit'),
    path('deposit/<int:deposit_id>/delete/', deposit_views.delete_deposit, name='delete-deposit'),
    # path('expenses/', expense_views.expense_list, name='expense-list'),
    # path('expense/<int:expense_id>/', expense_views.expense_detail, name='expense-detail'),
    # path('expense/create/', expense_views.create_expense, name='create-expense'),
    # path('expense/<int:expense_id>/update/', expense_views.update_expense, name='update-expense'),
    # path('expense/<int:expense_id>/delete/', expense_views.delete_expense, name='delete-expense'),
]
