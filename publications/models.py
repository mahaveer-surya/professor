from django.db import models

class Publication(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=500)
    authors = models.TextField()
    journal = models.CharField(max_length=300, blank=True)

    citation_count = models.IntegerField(default=0)

    # ✅ optional fields
    doi = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-year', '-citation_count']

    def __str__(self):
        return f"{self.title} ({self.year})"