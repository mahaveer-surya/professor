# core/context_processors.py
# This makes data available on ALL pages automatically.
from .models import SiteSettings, NavigationItem, Footer


def global_data(request):
    return {
        'site_settings': SiteSettings.load(),
        'nav_items': NavigationItem.objects.filter(is_active=True),
        'footer': Footer.load(),
    }