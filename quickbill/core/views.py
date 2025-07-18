from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserCreateForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def register_view(request):
    if request.method== 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
        return redirect('dashboard')
    else:
        form = UserCreateForm()    
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            nxt_url = request.GET.get('next')
            if nxt_url:                             # better approach to handle next URL
                return redirect(nxt_url)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form':form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return(redirect('home'))

@login_required
def dashboard(request):
    
    user = request.user
    if user.is_superuser:
        return render(request, 'core/admin_dashboard.html', {'user': user})
    else:
        return render(request, 'core/user_dashboard.html', {'user': user})
    
