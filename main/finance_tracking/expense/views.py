from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm, ExpenseSearchForm
from datetime import datetime, timedelta
from ..models import Category, Expense
from django.contrib import messages
import plotly.express as px
import pandas as pd

@login_required
def home(request):
    order_by = 'date'
    categories = Category.objects.filter(user=request.user, group='expense')
    form = ExpenseSearchForm()
    expenses = Expense.objects.filter(user=request.user)
    expense_id = request.GET.get('expense_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if expense_id:
        expenses = expenses.filter(pk=expense_id)
        order_by = 'search'
    elif start_date and end_date:
        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        expenses = expenses.filter(date__range=[start_date, end_date])
        order_by = 'search'
    elif start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.now().replace(day=1).date()
        expenses = expenses.filter(date__range=[start_date, end_date])
        order_by = 'search'
    else:
        end_date = datetime.now().replace(day=1).date()
        start_date = end_date - timedelta(days=30)
        expenses = expenses.filter(date__range=[start_date, end_date])
    expenses = expenses.order_by('-date')
    expenses_per_page = int(request.GET.get('expenses-per-page', 10))
    page = request.GET.get('page', 1)
    paginator = Paginator(expenses, expenses_per_page)
    try:
        expenses = paginator.page(page)
    except PageNotAnInteger:
        expenses = paginator.page(1)
    except EmptyPage:
        expenses = paginator.page(paginator.num_pages)
    line_data = {
        'Date': [expense.date for expense in expenses],
        'Amount': [expense.amount for expense in expenses],
    }
    line_df = pd.DataFrame(line_data)
    start_date = start_date.strftime('%B %m,%Y')
    end_date = end_date.strftime('%B %m,%Y')
    line_fig = px.line(
        line_df,
        x='Date',
        y='Amount',
        labels={'x': 'Date', 'y': 'Amount'},
        title=f'Expenses From {start_date} to {end_date}',
        line_shape='linear'
    )
    line_fig.update_layout(
        title=dict(
            text=f"Expenses From {start_date} to {end_date}",
            x=0.5
        )
    )
    chart = line_fig.to_html(full_html=False)
    context = {
        'categories': categories,
        'expenses': expenses,
        'current_order_by': order_by,
        'form': form,
        'chart':chart
    }
    return render(request, 'finance_tracking/expense/list.html', context)

@login_required
def expense_detail(request, expense_id):
    url = request.META.get('HTTP_REFERER', '/')
    if '/view/finances/' in url:
        return_url = 'view-finances'
    else:
        return_url = 'expense-home'
    expense = get_object_or_404(Expense, pk=expense_id)
    return render(request, 'finance_tracking/expense/detail.html', {'expense': expense, 'return_url': return_url})

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
    