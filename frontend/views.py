from django.shortcuts import render

def home(request):
    return render(request, 'frontend/index.html')


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
import json

@csrf_exempt  # Remove this if you use CSRF token in JS
def ajax_login_view(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

    try:
        data = json.loads(request.body)
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()

        print(password)
        print(email)

        if not email or not password:
            return JsonResponse({'status': 'error', 'message': 'Email and password are required'}, status=400)
        
        return JsonResponse({'status': 'success', 'redirect': '/'})

        # Authenticate using email as the username field
        # user = authenticate(request, username=email, password=password)

        # if user:
        #     login(request, user)
        #     return JsonResponse({'status': 'success', 'redirect': '/dashboard/'})  # or wherever
        # else:
        #     return JsonResponse({'status': 'error', 'message': 'Invalid email or password'}, status=401)

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
