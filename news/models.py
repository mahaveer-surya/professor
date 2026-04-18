# news/models.py
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()

    image = models.ImageField(upload_to="news/", blank=True, null=True)
    
    link = models.URLField(max_length=500, blank=True, null=True)  #  added field

    date = models.DateField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return self.title