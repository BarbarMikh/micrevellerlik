from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from camelion.models import ResultLog

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account:dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('account:login')

def dashboard_view(request):
    result_log = ResultLog.objects.filter(owner=request.user)

    context = {
        'result_log': result_log
    }
    return render(request, 'account/dashboard.html', context)
