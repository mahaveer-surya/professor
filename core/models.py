from django.db import models


# class SiteSettings(models.Model):
#     site_name = models.CharField(max_length=200)
#     logo = models.ImageField(upload_to="logo/", blank=True, null=True)

#     announcement_text = models.CharField(max_length=255, blank=True)
#     announcement_link = models.URLField(blank=True)

#     def __str__(self):
#         return self.site_name





# class Footer(models.Model):
#     content = models.TextField()

#     def __str__(self):
#         return "Footer Content"

# core/models.py

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class NavigationItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class SiteSettings(SingletonModel):
    site_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logo/", blank=True, null=True)
    announcement_text = models.CharField(max_length=255, blank=True)
    announcement_link = models.URLField(blank=True)

    def __str__(self):
        return "Site Settings"


class Footer(SingletonModel):
    content = models.TextField()

    def __str__(self):
        return "Footer"