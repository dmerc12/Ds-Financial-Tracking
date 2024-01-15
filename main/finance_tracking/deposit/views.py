from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DepositForm, DepositSearchForm
from django.contrib import messages
import plotly.express as px
import pandas as pd

from ..models import Category, Deposit
@login_required
def home(request):
    order_by = 'date'
    categories = Category.objects.filter(group='deposit')
    form = DepositSearchForm(user=request.user)
    deposits = Deposit.objects.filter(user=request.user)
    deposit_id = request.GET.get('deposit_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    category_id = request.GET.get('category_id')
    if deposit_id:
        deposits = deposits.filter(pk=deposit_id)
        order_by = 'search'
    elif start_date and end_date and category_id:
        deposits = deposits.filter(user=request.user, date__range=[start_date, end_date], category_id=category_id)
        order_by = 'search'
    elif start_date and end_date:
        deposits = deposits.filter(user=request.user, date__range=[start_date, end_date])
        order_by = 'search'
    elif category_id:
        deposits = deposits.filter(user=request.user, category_id=category_id)
        order_by = 'search'
    deposits = deposits.order_by('-date')
    deposits_per_page = int(request.GET.get('deposits-per-page', 10))
    page = request.GET.get('page', 1)
    paginator = Paginator(deposits, deposits_per_page)
    try:
        deposits = paginator.page(page)
    except PageNotAnInteger:
        deposits = paginator.page(1)
    except EmptyPage:
        deposits = paginator.page(paginator.num_pages)
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
        title='Deposits Over Time',
        line_shape='linear'
    )
    line_fig.update_layout(
        title=dict(
            text="Deposits Over Time",
            x=0.5
        )
    )
    chart = line_fig.to_html(full_html=False)
    context = {
        'categories': categories,
        'deposits': deposits,
        'current_order_by': order_by,
        'form': form,
        'chart':chart
    }
    return render(request, 'finance_tracking/deposit/list.html', context)

@login_required
def deposit_detail(request, deposit_id):
    url = request.META.get('HTTP_REFERER', '/')
    if '/view/finances/' in url:
        return_url = 'view-finances'
    else:
        return_url = 'deposit-home'
    deposit = get_object_or_404(Deposit, pk=deposit_id)
    return render(request, 'finance_tracking/deposit/detail.html', {'deposit': deposit, 'return_url': return_url})

@login_required
def create_deposit(request):
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

@login_required
def update_deposit(request, deposit_id):
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

@login_required
def delete_deposit(request, deposit_id):
    deposit = get_object_or_404(Deposit, pk=deposit_id)
    if request.method == 'POST':
        deposit.delete()
        messages.success(request, 'Deposit successfully deleted!')
        return redirect('deposit-home')
    return render(request, 'finance_tracking/deposit/delete.html', {'deposit': deposit})
    