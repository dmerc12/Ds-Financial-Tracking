from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render, redirect
from  django.contrib import messages

from .middleware import DepositMiddleware

from ..models import Category, Deposit

def home(request):
    try:
        categories = Category.objects.all()
    except RuntimeError as error:
        categories = []
        messages.warning(request, str(error))
    context = {'categories': categories}
    return render(request, 'finance_tracking/deposit/list.html', context)
