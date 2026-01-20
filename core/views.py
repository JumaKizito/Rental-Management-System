# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PropertyForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PropertyForm


# --------------------
# AUTH VIEWS
# --------------------

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'core/login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            messages.success(request, "Account created successfully! Login now.")
            return redirect('login')

    return render(request, 'core/signup.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


# --------------------
# DASHBOARD
# --------------------

@login_required(login_url='login')
def dashboard_view(request):
    pie_chart_data = [
        {'property': 'Apartment A', 'total_rent': 120000},
        {'property': 'Apartment B', 'total_rent': 90000},
        {'property': 'House C', 'total_rent': 150000},
        {'property': 'Shop D', 'total_rent': 80000},
    ]

    bar_chart_data = [
        {'month': 'Aug', 'amount': 320000},
        {'month': 'Sep', 'amount': 350000},
        {'month': 'Oct', 'amount': 300000},
        {'month': 'Nov', 'amount': 420000},
        {'month': 'Dec', 'amount': 450000},
    ]

    context = {
        'total_properties': 12,
        'total_tenants': 34,
        'active_leases': 28,
        'monthly_income': 450000,
        'pie_labels': [p['property'] for p in pie_chart_data],
        'pie_values': [p['total_rent'] for p in pie_chart_data],
        'bar_labels': [b['month'] for b in bar_chart_data],
        'bar_values': [b['amount'] for b in bar_chart_data],
    }

    return render(request, 'core/dashboard.html', context)


# --------------------
# PROPERTIES PAGE
# --------------------




@login_required(login_url='login')
def properties_view(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('properties')  # later change to list page
    else:
        form = PropertyForm()

    return render(request, 'core/create_property.html', {'form': form})


