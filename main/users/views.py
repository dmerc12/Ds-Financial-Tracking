from .forms import RegisterForm, LoginForm, UpdateUserForm, ChangePasswordForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CustomUser

# Login view 
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {user.first_name}!')
                return redirect('home')
            else:
                messages.error(request, 'Incorrect username or password, please try again!')
                return redirect('login')
        else:
            messages.error(request, 'Incorrect username or password, please try again!')
            return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    
# Logout view
def logout_user(request):
    logout(request)
    messages.success(request, 'Goodbye!')
    return redirect('login')

# Register view for users
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            user = form.save()
            CustomUser.objects.create(user=user, phone_number=phone_number)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been successfully registered! Welcome!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Update user view
def update_user(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        current_user = CustomUser.objects.get(user=user.id)
        form = UpdateUserForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            current_user.phone_number = form.cleaned_data['phone_number']
            current_user.save()
            login(request, user)
            messages.success(request, 'Your profile has been successfully updated!')
            return redirect('home')
        else:
            form.initial['phone_number'] = current_user.phone_number
        return render(request, 'users/update.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')
    
# Change password view
def change_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                login(request, current_user)
                messages.success(request, 'Your password has been changed!')
                return redirect('home')
        else:
            form = ChangePasswordForm(current_user)
        return render(request, 'users/change_password.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')

def delete_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.user.delete()
            logout(request)
            messages.success(request, 'Your profile has been successfully deleted, goodbye!')
            return redirect('login')
        return render(request, 'users/delete.html')
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')
    