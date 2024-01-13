from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CategoryForm
from ..models import Category

def create_category(request):
    return_url = request.META.get('HTTP_REFERER', '/')
    group = 'deposit' if '/deposits/' in return_url else 'expense' if '/expenses/' in return_url else ''
    if request.method == 'POST':
        form = CategoryForm(request.POST, initial={'group': group})
        if form.is_valid():
            category = Category()
            category = Category(**form.cleaned_data)
            category.user = request.user
            category.save()
            messages.success(request, 'Category successfully created!')
            return redirect(f'{form.cleaned_data["group"]}-home')
    else:
        form = CategoryForm(initial={'group': group})
    return render(request, 'finance_tracking/category/create.html', {'form': form, 'action': 'create'})

def update_category(request, category_id):
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
    return render(request, 'finance_tracking/category/update.html', {'form': form, 'action': 'update', 'category': category})

def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    group = category.group
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category successfully deleted!')
        return redirect(f'{group}-home')
    return render(request, 'finance_tracking/category/delete.html', {'category': category, 'group': group})
