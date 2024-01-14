from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.functions import TruncMonth, TruncYear
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ExpenseForm

from ..models import Category, Expense

@login_required
def home(request):
    try:
        categories = Category.objects.filter(group='expense') 
        expenses = Expense.objects.filter(user=request.user).annotate(order_date=TruncMonth('date')).order_by('-date')
        expenses_per_page = int(request.GET.get('expenses-per-page', 10))
        page = request.GET.get('page', 1)
        paginator = Paginator(expenses, expenses_per_page)
        try:
            expenses = paginator.page(page)
        except PageNotAnInteger:
            expenses = paginator.page(1)
        except EmptyPage:
            expenses = paginator.page(paginator.num_pages)
    except RuntimeError as error:
        categories = []
        messages.warning(request, str(error))
    context = {'categories': categories, 'expenses': expenses, 'current_order_by': 'month'}
    return render(request, 'finance_tracking/expense/list.html', context)

@login_required
def home_by_category(request):
    try:
        categories = Category.objects.filter(group='expense')
        expenses = Expense.objects.filter(user=request.user).order_by('category')
        expenses_per_page = int(request.GET.get('expenses-per-page', 10))
        page = request.GET.get('page', 1)
        paginator = Paginator(expenses, expenses_per_page)
        try:
            expenses = paginator.page(page)
        except PageNotAnInteger:
            expenses = paginator.page(1)
        except EmptyPage:
            expenses = paginator.page(paginator.num_pages)
    except RuntimeError as error:
        categories = []
        messages.warning(request, str(error))
    context = {'categories': categories, 'expenses': expenses, 'current_order_by': 'category'}
    return render(request, 'finance_tracking/expense/list.html', context)

@login_required
def search_expenses(request):
    try:
        categories = Category.objects.filter(group='expense')
        expense_id = request.GET.get('expense_id')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        category_id = request.GET.get('category_id')
        expenses = Expense.objects.filter(user=request.user)
        if expense_id:
            expenses = expenses.filter(pk=expense_id)
        elif start_date and end_date:
            expenses = expenses.filter(date__range=[start_date, end_date])
        elif category_id:
            expenses = expenses.filter(category_id=category_id)
        expenses_per_page = int(request.GET.get('expenses-per-page', 10))
        page = request.GET.get('page', 1)
        paginator = Paginator(expenses, expenses_per_page)
        try:
            expenses = paginator.page(page)
        except PageNotAnInteger:
            expenses = paginator.page(1)
        except EmptyPage:
            expenses = paginator.page(paginator.num_pages)
    except RuntimeError as error:
        categories = []
        messages.warning(request, str(error.message))
    context = {'categories': categories, 'expenses': expenses, 'current_order_by': 'search'}
    return render(request, 'finance_tracking/expense/list.html', context)

@login_required
def expense_detail(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    return render(request, 'finance_tracking/expense/detail.html', {'expense': expense})

@login_required
def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        form.fields['category'].queryset = Category.objects.filter(group='expense')
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense successfully created!')
            return redirect('expense-home')
    else:
        form = ExpenseForm()
        form.fields['category'].queryset = Category.objects.filter(group='expense')
    return render(request, 'finance_tracking/expense/create.html', {'form': form, 'action': 'create'})

@login_required
def update_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense successfully updated!')
            return redirect('expense-home')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'finance_tracking/expense/update.html', {'form': form, 'action': 'update', 'expense': expense})

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense successfully deleted!')
        return redirect('expense-home')
    return render(request, 'finance_tracking/expense/delete.html', {'expense': expense})
    