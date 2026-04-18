from import_export import resources
from .models import Publication

class PublicationResource(resources.ModelResource):
    class Meta:
        model = Publication
        import_id_fields = ('title',)  # or ('doi',) if unique
        fields = (
            'year',
            'title',
            'authors',
            'journal',
            'citation_count',
            'doi',
            'link',
        )