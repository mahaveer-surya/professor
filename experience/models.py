# experience/models.py
from django.db import models


class Experience(models.Model):
    position = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    description = models.TextField(blank=True)

    is_current = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} - {self.organization}"