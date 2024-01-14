from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def home(request):
    user = User.objects.get(pk=request.user.pk)
    return render(request, 'users/home.html', {'user': user})

def register(request):
    try:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('login')
        else:
            form = UserRegisterForm()
    except RuntimeError as error:
        messages.error(request, str(error.message))
    return render(request, 'users/register.html', {'form':  form})

@login_required
def update_user(request):
    try:
        if request.method == 'POST':
            form = UserUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Your account has been updated!")
                return redirect('user-home')
        else:
            form = UserUpdateForm(instance=request.user)
    except RuntimeError as error:
        messages.error(request, str(error.message))
    return render(request, 'users/update.html', {'form': form})

@login_required
def change_password(request):
    try:
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been changed!")
                return redirect('user-home')
            else:
                messages.error(request, 'There was an error changing your password, please try again!')
        else:
            form = PasswordChangeForm(user=request.user)
    except RuntimeError as error:
        messages.error(request, str(error.message))
    return render(request, 'users/change_password.html', {'form': form})
        
@login_required
def delete_user(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Your account has been deleted, goodbye')
        return redirect('login')
    return render(request, 'users/delete.html')
