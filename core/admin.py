
from django.contrib import admin
from .models import SiteSettings, NavigationItem, Footer


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Footer.objects.exists()


@admin.register(NavigationItem)
class NavigationItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')