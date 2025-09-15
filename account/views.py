from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

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

@login_required
def logout_view(request):
    logout(request)
    return redirect('account:login')

@login_required
def dashboard_view(request):
    result_logs = ResultLog.objects.filter(owner=request.user).order_by('-created_on')

    # Pagination
    paginator = Paginator(result_logs, 20) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'account/dashboard.html', context)


@login_required
def log_details_view(request, pk):
    result_log = ResultLog.objects.get(pk=pk)
    context = {
        'result_log': result_log,
    }
    return render(request, 'account/log_details.html', context)