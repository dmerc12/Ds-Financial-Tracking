from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import DepositForm

from ..models import Category, Deposit

def home(request):
    try:
        categories = Category.objects.filter(group='deposit')
        deposits = Deposit.objects.all()
    except RuntimeError as error:
        categories = []
        messages.warning(request, str(error))
    context = {'categories': categories, 'deposits': deposits}
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
