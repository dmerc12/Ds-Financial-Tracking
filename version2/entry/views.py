from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Home view
@login_required
def home(request):
    return render(request, 'entry/home.html')
    