from django.shortcuts import render, get_object_or_404, redirect
from ..models import Category, Deposit
from django.contrib import messages
from .forms import CategoryForm
from ..models import *

# Create category view
def create_category(request, group):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                category = form.save(commit=False)
                category.user = request.user
                category.group = group
                category.save()
                messages.success(request, 'Category successfully created!')
                return redirect(f'{category.group}-home')
        else:
            form = CategoryForm(initial={'group': group})
        return render(request, 'finance_tracking/category/create.html', {'form': form, 'group': group})
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')

# Update category view
def update_category(request, category_id):
    if request.user.is_authenticated:
        return_url = request.META.get('HTTP_REFERER', '/')
        group = 'deposit' if '/deposits/' in return_url else 'expense' if '/expenses/' in return_url else ''
        category = get_object_or_404(Category, pk=category_id)
        if request.method == 'POST':
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                messages.success(request, 'Category successfully updated!')
                return redirect(f'{form.cleaned_data["group"]}-home')
        else:
            form = CategoryForm(initial={'group': group}, instance=category)
        return render(request, 'finance_tracking/category/update.html', {'form': form, 'category': category})
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')

# Delete category view
def delete_category(request, category_id):
    if request.user.is_authenticated:
        category = get_object_or_404(Category, pk=category_id)
        if request.method == 'POST':
            related_deposits = Deposit.objects.filter(category=category)
            related_expenses = Expense.objects.filter(category=category)
            if (len(related_deposits) == 0) and (len(related_expenses) == 0):
                category.delete()
                messages.success(request, 'Category successfully deleted!')
                return redirect(f'{category.group}-home')
            else:
                messages.error(request, 'Category is currently being used and cannot be deleted!')
                return redirect(f'{category.group}-home')
        return render(request, 'finance_tracking/category/delete.html', {'category': category, 'group': category.group})
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')
