# alumni/models.py
from django.db import models


class Alumni(models.Model):
    CATEGORY_CHOICES = (
        ('current', 'Current Alumni'),
        ('passed', 'Pass Out Alumni'),
    )

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    designation = models.CharField(max_length=200, blank=True)
    organization = models.CharField(max_length=200, blank=True)

    photo = models.ImageField(upload_to="alumni/", blank=True, null=True)

    passing_year = models.IntegerField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.category})"