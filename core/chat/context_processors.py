from products.models import Business  # Import your Store model
from django.conf import settings


def store_context(request):
    stores = Business.objects.all()  # Fetch all stores
    return {
        'stores': stores,  # Make it available in all templates
        'recaptcha_site_key': getattr(settings, 'RECAPTCHA_SITE_KEY', ''),
    }
