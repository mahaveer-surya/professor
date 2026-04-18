from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Publication
from .resources import PublicationResource

@admin.register(Publication)
class PublicationAdmin(ImportExportModelAdmin):
    resource_class = PublicationResource
    list_display = ('title', 'year', 'journal', 'citation_count')
    search_fields = ('title', 'authors', 'journal')