from django.shortcuts import render
from .models import Deposit, Expense
from django.db.models import Sum
from .forms import SearchForm

def view_finances(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            deposits = Deposit.objects.filter(user=request.user, date__range=[start_date, end_date])
            expenses = Expense.objects.filter(user=request.user, date__range=[start_date, end_date])
    else:
        form = SearchForm()
        deposits = Deposit.objects.filter(user=request.user)
        expenses = Expense.objects.filter(user=request.user)
    total_income = deposits.aggregate(total=Sum('amount'))['total'] or 0.00
    total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0.00
    context = {
        'deposits': deposits,
        'expenses': expenses,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'form': form
    }
    return render(request, 'finance_tracking/manage_finances.html', context)
    