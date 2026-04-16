# publications/admin.py
from django.contrib import admin
from .models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'journal')
    list_filter = ('year', 'journal')
    search_fields = ('title', 'authors')