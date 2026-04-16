# experience/admin.py
from django.contrib import admin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'organization', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current', 'organization')
    search_fields = ('position', 'organization')