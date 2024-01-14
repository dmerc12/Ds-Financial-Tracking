from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models.functions import TruncMonth, TruncYear
from django.contrib import messages
from django.shortcuts import render
from .models import Deposit, Expense
from django.db.models import Sum
from itertools import chain

@login_required
def view_finances(request):
    try:
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
    total_income = deposits.aggregate(total=Sum('amount'))['total'] or 0.00
    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0.00
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'current_order_by': 'month'
    }
    return render(request, 'finance_tracking/manage_finances.html', context)

@login_required
def view_finances_by_category(request):
    try:
        deposits = Deposit.objects.filter(user=request.user).order_by('category')
        expenses = Expense.objects.filter(user=request.user).order_by('category')
        transactions_per_page = int(request.GET.get('transactions-per-page', 10))
        transactions = list(deposits) + list(expenses)
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
    total_income = deposits.aggregate(total=Sum('amount'))['total'] or 0.00
    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0.00
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'current_order_by': 'category'
    }
    return render(request, 'finance_tracking/manage_finances.html', context)

@login_required
def search_finances(request):
    try:
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        category_id = request.GET.get('category_id')
        deposits = Deposit.objects.filter(user=request.user)
        expenses = Expense.objects.filter(user=request.user)
        if start_date and end_date:
            deposits = deposits.filter(date__range=[start_date, end_date])
            expenses = expenses.filter(date__range=[start_date, end_date])
        elif category_id:
            deposits = deposits.filter(category_id=category_id)
            expenses = expenses.filter(category_id=category_id)
        transactions_per_page = int(request.GET.get('transactions-per-page', 10))
        transactions = sorted(chain(deposits, expenses), key=lambda transaction: transaction.date, reverse=True)
        page = request.GET.get('page', 1)
        paginator = Paginator(expenses, transactions_per_page)
        try:
            transactions = paginator.page(page)
        except PageNotAnInteger:
            transactions = paginator.page(page)
        except EmptyPage:
            transactions = paginator.page(paginator.num_pages)
    except RuntimeError as error:
        transactions = []
        messages.warning(request, str(error.message))
    total_income = deposits.aggregate(total=Sum('amount'))['total'] or 0.00
    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0.00
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'current_order_by': 'search'
    }
    return render(request, 'finance_tracking/expense/list.html', context)
