# publications/models.py
from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=500)
    authors = models.TextField(help_text="Comma-separated authors")
    journal = models.CharField(max_length=300, blank=True)

    year = models.IntegerField()

    doi = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True)

    abstract = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-year', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.year})"