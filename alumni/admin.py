# alumni/admin.py
from django.contrib import admin
from .models import Alumni


@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'passing_year', 'is_active')
    list_filter = ('category', 'passing_year')
    search_fields = ('name', 'organization')
    list_editable = ('is_active',)