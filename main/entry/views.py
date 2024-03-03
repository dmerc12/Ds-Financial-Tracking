from django.shortcuts import render, redirect
from django.contrib import messages

# Home view
def home(request):
    if request.user.is_authenticated:
        return render(request, 'entry/home.html')
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')
    