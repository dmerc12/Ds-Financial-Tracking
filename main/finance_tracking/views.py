from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import Deposit, Expense
from django.contrib import messages
from django.db.models import Sum
from .forms import SearchForm
from itertools import chain
import plotly.express as px
import pandas as pd

# Finance tracking home view
def home(request):
    if request.user.is_authenticated:
        return render(request, 'finance_tracking/home.html')
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')

# View finances view
def view_finances(request):
    if request.user.is_authenticated:
        form = SearchForm(request.GET or None)
        deposits = Deposit.objects.filter(user=request.user)
        expenses = Expense.objects.filter(user=request.user)
        transactions = sorted(chain(deposits, expenses), key=lambda transaction: transaction.date, reverse=True)
        transactions_per_page = int(request.GET.get('transactions-per-page', 10))
        paginator = Paginator(transactions, transactions_per_page)
        page = request.GET.get('page', 1)
        try:
            transactions = paginator.page(page)
        except (PageNotAnInteger, EmptyPage):
            transactions = paginator.page(paginator.num_pages)
        # Calculate total income and expenses
        total_income = sum(transaction.amount for transaction in transactions if isinstance(transaction, Deposit))
        total_expenses = sum(transaction.amount for transaction in transactions if isinstance(transaction, Expense))
        # Bar chart
        bar_fig = px.bar(
            x=['Income', 'Expenses'],
            y=[total_income, total_expenses],
            labels={'x': 'Category', 'y': 'Amount'},
            title="Financial Overview",
            color=['Income', 'Expenses'],
            color_discrete_map={'Income': 'green', 'Expenses': 'red'}
        )
        bar_fig.update_layout(title=dict(text="Financial Overview", x=0.5))
        bar_chart = bar_fig.to_html(full_html=False)
        # Line chart
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
        line_fig.update_layout(title=dict(text="Deposits vs Expenses Over Time", x=0.5))
        line_chart = line_fig.to_html(full_html=False)
        context = {
            'form': form,
            'transactions': transactions,
            'total_income': total_income,
            'total_expenses': total_expenses,
            'bar_chart': bar_chart,
            'line_chart': line_chart,
        }
        return render(request, 'finance_tracking/view_finances.html', context)
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')

# Analyze finances view
def analyze_finances(request):
    if request.user.is_authenticated:
        form = SearchForm(request.GET or None)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
        else:
            # Default to the most recent month
            end_date = datetime.now().replace(day=1)
            start_date = end_date - timedelta(days=30)
        expenses = Expense.objects.filter(date__range=[start_date, end_date])
        deposits = Deposit.objects.filter(date__range=[start_date, end_date])
        # Calculate totals for expenses and deposits by category
        expense_totals_by_category = expenses.values('category__name').annotate(total=Sum('amount')).order_by('category__name')
        deposit_totals_by_category = deposits.values('category__name').annotate(total=Sum('amount')).order_by('category__name')
        # Calculate total income and expenses
        total_income = deposits.aggregate(total=Sum('amount'))['total'] or 0
        total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0
        # Calculate gross income/loss
        gross_income_loss = total_income - total_expenses
        # Pie charts for analyze_finances
        expense_pie_data = {
            'Category': [transaction.category.name for transaction in expenses],
            'Amount': [transaction.amount for transaction in expenses]
        }
        income_pie_data = {
            'Category': [transaction.category.name for transaction in deposits],
            'Amount': [transaction.amount for transaction in deposits]
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
            'expense_totals_by_category': expense_totals_by_category,
            'deposit_totals_by_category': deposit_totals_by_category,
            'total_income': total_income,
            'total_expenses': total_expenses,
            'gross_income_loss': gross_income_loss,
            'income_pie_chart': income_pie_chart,
            'expense_pie_chart': expense_pie_chart,
        }
        return render(request, 'finance_tracking/analyze_finances.html', context)
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')
