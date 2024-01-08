from django.shortcuts import render, get_object_or_404, redirect
from .middleware import CategoryMiddleware
from django.contrib import messages
from .forms import CategoryForm
from ..models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'finance_tracking/category/list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'finance_tracking/category/detail.html', {'category', category})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            CategoryMiddleware.create_category(request, form)
            return redirect('category-list')