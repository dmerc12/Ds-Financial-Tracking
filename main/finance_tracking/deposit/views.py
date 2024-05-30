from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Category, Deposit
from django.contrib import messages
from collections import defaultdict
from django.db.models import Sum
from datetime import datetime
import plotly.express as px
from .forms import *
import pandas as pd

# Deposit home view
def home(request):
    if request.user.is_authenticated:
        categories = Category.objects.filter(group='deposit', user=request.user)
        form = DepositSearchForm()
        deposits = Deposit.objects.filter(user=request.user)
        order_by = 'date'
        if request.method == 'POST':
            form = DepositSearchForm(request.POST)
            if form.is_valid():
                deposit_id = form.cleaned_data['deposit_id']
                start_date = form.cleaned_data['start_date']
                end_date = form.cleaned_data['end_date']
                if deposit_id:
                    deposits = deposits.filter(pk=deposit_id)
                    order_by = 'search'
                elif start_date and end_date:
                    deposits = deposits.filter(date__range=[start_date, end_date])
                    order_by = 'search'
                elif start_date:
                    end_date = datetime.now().replace(day=1).date()
                    deposits = deposits.filter(date__range=[start_date, end_date])
                    order_by = 'search'
        deposits = deposits.order_by('-date')
        # Line chart showing deposits over time
        line_data = {
            'Date': [deposit.date for deposit in deposits],
            'Amount': [deposit.amount for deposit in deposits],
        }
        line_df = pd.DataFrame(line_data)
        line_fig = px.line(
            line_df,
            x='Date',
            y='Amount',
            labels={'x': 'Date', 'y': 'Amount'},
            title=f'Deposits Over Time',
            line_shape='linear'
        )
        line_fig.update_layout(
            title=dict(
                text=f"Deposits Over Time",
                x=0.5
            )
        )
        line_chart = line_fig.to_html(full_html=False)
        # Pie chart showing deposits by cateogry
        total_deposit_amount = deposits.aggregate(total=Sum('amount'))['total'] or 0
        category_totals = defaultdict(float)
        for deposit in deposits:
            category_totals[deposit.category.name] += deposit.amount
        category_percentages = {category: (amount / total_deposit_amount) * 100 for category, amount in category_totals.items()}
        pie_data = {
            'Category': list(category_percentages.keys()),
            'Total Amount': list(category_totals.values()),
            'Percentage': list(category_percentages.values())
        }
        pie_df = pd.DataFrame(pie_data)
        hover_data = ['Total Amount']
        pie_fig = px.pie(
            pie_df,
            names='Category',
            values='Percentage',
            title='Deposits By Category',
            hover_data=hover_data
        )
        pie_fig.update_layout(
            title=dict(
                text='Deposits By Category',
                x=0.5
            )
        )
        pie_chart = pie_fig.to_html(full_html=False)
        deposits_per_page = int(request.GET.get('deposits-per-page', 10))
        page = request.GET.get('page', 1)
        paginator = Paginator(deposits, deposits_per_page)
        try:
            deposits = paginator.page(page)
        except (PageNotAnInteger, EmptyPage):
            deposits = paginator.page(1)
        context = {
            'categories': categories,
            'deposits': deposits,
            'current_order_by': order_by,
            'form': form,
            'pie_chart':pie_chart,
            'line_chart': line_chart
        }
        return render(request, 'finance_tracking/deposit/list.html', context)
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')

# Deposit detail view
def deposit_detail(request, deposit_id):
    if request.user.is_authenticated:
        url = request.META.get('HTTP_REFERER', '/')
        if '/view/finances/' in url:
            return_url = 'view-finances'
        else:
            return_url = 'deposit-home'
        deposit = get_object_or_404(Deposit, pk=deposit_id)
        return render(request, 'finance_tracking/deposit/detail.html', {'deposit': deposit, 'return_url': return_url})
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')

# Create deposit view
def create_deposit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DepositForm(request.POST)
            form.fields['category'].queryset = Category.objects.filter(group='deposit')
            if form.is_valid():
                deposit = form.save(commit=False)
                deposit.user = request.user
                deposit.save()
                messages.success(request, 'Deposit successfully created!')
                return redirect('deposit-home')
        else:
            form = DepositForm()
            form.fields['category'].queryset = Category.objects.filter(group='deposit')
        return render(request, 'finance_tracking/deposit/create.html', {'form': form, 'action': 'create'})
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')

# Update deposit view
def update_deposit(request, deposit_id):
    if request.user.is_authenticated:
        deposit = get_object_or_404(Deposit, pk=deposit_id)
        if request.method == 'POST':
            form = DepositForm(request.POST, instance=deposit)
            if form.is_valid():
                form.save()
                messages.success(request, 'Deposit successfully updated!')
                return redirect('deposit-home')
        else:
            form = DepositForm(instance=deposit)
        return render(request, 'finance_tracking/deposit/update.html', {'form': form, 'action': 'update', 'deposit': deposit})
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')

# Delete deposit view
def delete_deposit(request, deposit_id):
    if request.user.is_authenticated:
        deposit = get_object_or_404(Deposit, pk=deposit_id)
        if request.method == 'POST':
            deposit.delete()
            messages.success(request, 'Deposit successfully deleted!')
            return redirect('deposit-home')
        return render(request, 'finance_tracking/deposit/delete.html', {'deposit': deposit})
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')
