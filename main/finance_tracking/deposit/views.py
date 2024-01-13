from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.functions import TruncMonth, TruncYear
from django.contrib import messages
from .forms import DepositForm

from ..models import Category, Deposit

def home(request):
    try:
        categories = Category.objects.filter(group='deposit') 
        deposits = Deposit.objects.filter(user=request.user).annotate(order_date=TruncMonth('date')).order_by('-date')
    except RuntimeError as error:
        categories = []
        messages.warning(request, str(error))
    context = {'categories': categories, 'deposits': deposits, 'current_order_by': 'month'}
    return render(request, 'finance_tracking/deposit/list.html', context)

def home_by_year(request):
    try:
        categories = Category.objects.filter(group='deposit')
        deposits = Deposit.objects.filter(user=request.user).annotate(order_date=TruncYear('date')).order_by('-order_date', '-date')
    except RuntimeError as error:
        categories = []
        messages.warning(request, str(error))
    context = {'categories': categories, 'deposits': deposits, 'current_order_by': 'year'}
    return render(request, 'finance_tracking/deposit/list.html', context)

def home_by_category(request):
    try:
        categories = Category.objects.filter(group='deposit')
        deposits = Deposit.objects.filter(user=request.user).order_by('category')
    except RuntimeError as error:
        categories = []
        messages.warning(request, str(error))
    context = {'categories': categories, 'deposits': deposits, 'current_order_by': 'category'}
    return render(request, 'finance_tracking/deposit/list.html', context)

def search_deposits(request):
    categories = Category.objects.filter(group='deposit')
    deposit_id = request.GET.get('deposit_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    category_id = request.GET.get('category_id')

    deposits = Deposit.objects.filter(user=request.user)

    if deposit_id:
        deposits = deposits.filter(pk=deposit_id)
    elif start_date and end_date:
        deposits = deposits.filter(date__range=[start_date, end_date])
    elif category_id:
        deposits = deposits.filter(category_id=category_id)

    context = {'categories': categories, 'deposits': deposits, 'current_order_by': 'search'}
    return render(request, 'finance_tracking/deposit/list.html', context)

def deposit_detail(request, deposit_id):
    deposit = get_object_or_404(Deposit, pk=deposit_id)
    return render(request, 'finance_tracking/deposit/detail.html', {'deposit': deposit})

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

def delete_deposit(request, deposit_id):
    deposit = get_object_or_404(Deposit, pk=deposit_id)
    if request.method == 'POST':
        deposit.delete()
        messages.success(request, 'Deposit successfully deleted!')
        return redirect('deposit-home')
    return render(request, 'finance_tracking/deposit/delete.html', {'deposit': deposit})
    