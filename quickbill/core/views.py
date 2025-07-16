from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserCreateForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def register_view(request):
    if request.method== 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save
            login(request, user)
            messages.success(request, 'Registration successful.')
        return redirect('home')
    else:
        form = UserCreateForm()    
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages(request, 'Login successful.')
        return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form':form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return(redirect('home'))