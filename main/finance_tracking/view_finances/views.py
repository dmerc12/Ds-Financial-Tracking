from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncMonth
from ..models import Deposit, Expense
from django.contrib import messages
from django.shortcuts import render
from .forms import SearchForm
from itertools import chain
import plotly.express as px
import pandas as pd

@login_required
def view_finances(request):
    try:
        form = SearchForm(request.GET)
        deposits = Deposit.objects.filter(user=request.user).annotate(ordate_date=TruncMonth('date')).order_by('-date')
        expenses = Expense.objects.filter(user=request.user).annotate(order_by=TruncMonth('date')).order_by('-date')
        transactions_per_page = int(request.GET.get('transactions-per-page', 10))
        transactions = sorted(chain(deposits, expenses), key=lambda transaction: transaction.date, reverse=True)
        page = request.GET.get('page', 1)
        paginator = Paginator(transactions, transactions_per_page)
        try:
            transactions = paginator.page(page)
        except PageNotAnInteger:
            transactions = paginator.page(page)
        except EmptyPage:
            transactions = paginator.page(paginator.num_pages)
    except RuntimeError as error:
        transactions = []
        messages.error(request, str(error))
    total_income = sum(transaction.amount for transaction in transactions if isinstance(transaction, Deposit))
    total_expenses = sum(transaction.amount for transaction in transactions if isinstance(transaction, Expense))
    bar_fig = px.bar(
        x=['Income', 'Expenses'], 
        y=[total_income, total_expenses], 
        labels={'x': 'Category', 'y': 'Amount'},
        title="Financial Overview",
        color=['Income', 'Expenses'],
        color_discrete_map={'Income': 'green', 'Expenses': 'red'}
    )
    bar_fig.update_layout(
        title=dict(
            text="Financial Overview",
            x=0.5
        )
    )
    bar_chart = bar_fig.to_html(full_html=False)
    line_data = {
        'Date': [transaction.date for transaction in transactions],
        'Amount': [transaction.amount for transaction in transactions],
        'Type': ['Deposit' if isinstance(transaction, Deposit) else 'Expense' for transaction in transactions],
    }
    line_df = pd.DataFrame(line_data)
    line_fig = px.line(
        line_df,
        x='Date',
        y='Amount',
        color='Type',
        labels={'x': 'Date', 'y': 'Amount'},
        title='Deposits vs Expenses Over Time',
        line_shape='linear'
    )
    line_fig.update_layout(
        title=dict(
            text="Deposits vs Expenses Over Time",
            x=0.5
        )
    )
    line_chart = line_fig.to_html(full_html=False)
    expense_pie_data = {
        'Category': [transaction.category.name for transaction in transactions if isinstance(transaction, Expense)],
        'Amount': [transaction.amount for transaction in transactions if isinstance(transaction, Expense)]
    }
    income_pie_data = {
        'Category': [transaction.category.name for transaction in transactions if isinstance(transaction, Deposit)],
        'Amount': [transaction.amount for transaction in transactions if isinstance(transaction, Deposit)]
    }
    expense_pie_df = pd.DataFrame(expense_pie_data)
    income_pie_df = pd.DataFrame(income_pie_data)
    expense_pie_fig = px.pie(
        expense_pie_df,
        names='Category',
        values='Amount',
        title='Total Expenses By Category'
    )
    expense_pie_fig.update_layout(
        title=dict(
            text="Total Expenses By Category",
            x=0.5
        )
    )
    income_pie_fig = px.pie(
        income_pie_df,
        names='Category',
        values='Amount',
        title='Total Income By Category'
    )
    income_pie_fig.update_layout(
        title=dict(
            text="Total Income By Category",
            x=0.5
        )
    )
    expense_pie_chart = expense_pie_fig.to_html(full_html=False)
    income_pie_chart = income_pie_fig.to_html(full_html=False)
    context = {
        'form': form,
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'current_order_by': 'month',
        'bar_chart': bar_chart,
        'line_chart': line_chart,
        'income_pie_chart': income_pie_chart,
        'expense_pie_chart': expense_pie_chart
    }
    return render(request, 'finance_tracking/view_finances.html', context)

@login_required
def search_finances(request):
    try:
        form = SearchForm(request.GET)
        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
        deposits = Deposit.objects.filter(user=request.user)
        expenses = Expense.objects.filter(user=request.user)
        if start_date and end_date:
            deposits = deposits.filter(date__range=[start_date, end_date])
            expenses = expenses.filter(date__range=[start_date, end_date])
        transactions_per_page = int(request.GET.get('transactions-per-page', 10))
        transactions = sorted(chain(deposits, expenses), key=lambda transaction: transaction.date, reverse=True)
        page = request.GET.get('page', 1)
        paginator = Paginator(transactions, transactions_per_page)
        try:
            transactions = paginator.page(page)
        except PageNotAnInteger:
            transactions = paginator.page(page)
        except EmptyPage:
            transactions = paginator.page(paginator.num_pages)
    except RuntimeError as error:
        transactions = []
        messages.warning(request, str(error.message))
    total_income = sum(transaction.amount for transaction in transactions if isinstance(transaction, Deposit))
    total_expenses = sum(transaction.amount for transaction in transactions if isinstance(transaction, Expense))
    bar_fig = px.bar(
        x=['Income', 'Expenses'], 
        y=[total_income, total_expenses], 
        labels={'x': 'Category', 'y': 'Amount'},
        title="Financial Overview",
        color=['Income', 'Expenses'],
        color_discrete_map={'Income': 'green', 'Expenses': 'red'}
    )
    bar_fig.update_layout(
        title=dict(
            text="Financial Overview",
            x=0.5
        )
    )
    bar_chart = bar_fig.to_html(full_html=False)
    line_data = {
        'Date': [transaction.date for transaction in transactions],
        'Amount': [transaction.amount for transaction in transactions],
        'Type': ['Deposit' if isinstance(transaction, Deposit) else 'Expense' for transaction in transactions],
    }
    line_df = pd.DataFrame(line_data)
    line_fig = px.line(
        line_df,
        x='Date',
        y='Amount',
        color='Type',
        labels={'x': 'Date', 'y': 'Amount'},
        title='Deposits vs Expenses Over Time',
        line_shape='linear'
    )
    line_fig.update_layout(
        title=dict(
            text="Deposits vs Expenses Over Time",
            x=0.5
        )
    )
    line_chart = line_fig.to_html(full_html=False)
    expense_pie_data = {
        'Category': [transaction.category.name for transaction in transactions if isinstance(transaction, Expense)],
        'Amount': [transaction.amount for transaction in transactions if isinstance(transaction, Expense)]
    }
    income_pie_data = {
        'Category': [transaction.category.name for transaction in transactions if isinstance(transaction, Deposit)],
        'Amount': [transaction.amount for transaction in transactions if isinstance(transaction, Deposit)]
    }
    expense_pie_df = pd.DataFrame(expense_pie_data)
    income_pie_df = pd.DataFrame(income_pie_data)
    expense_pie_fig = px.pie(
        expense_pie_df,
        names='Category',
        values='Amount',
        title='Total Expenses By Category'
    )
    expense_pie_fig.update_layout(
        title=dict(
            text="Total Expenses By Category",
            x=0.5
        )
    )
    income_pie_fig = px.pie(
        income_pie_df,
        names='Category',
        values='Amount',
        title='Total Income By Category'
    )
    income_pie_fig.update_layout(
        title=dict(
            text="Total Income By Category",
            x=0.5
        )
    )
    expense_pie_chart = expense_pie_fig.to_html(full_html=False)
    income_pie_chart = income_pie_fig.to_html(full_html=False)
    context = {
        'form': form,
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'current_order_by': 'search',
        'bar_chart': bar_chart,
        'line_chart': line_chart,
        'income_pie_chart': income_pie_chart,
        'expense_pie_chart': expense_pie_chart
    }
    return render(request, 'finance_tracking/view_finances.html', context)
