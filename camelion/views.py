from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import tldextract

def camelion_view(request):

    existing_email = request.GET.get('em', '').strip()
    email_is_valid = False
    domain = None

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
        email_is_valid = False

    context = {
        'existing_email': existing_email,
        'email_is_valid': email_is_valid,
        'logo_text': base_domain,
        'domain':domain,
    }
    return render(request, 'camelion/camelion_one.html', context)