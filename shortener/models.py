from django.db import models


class ShortLink(models.Model):
    url = models.URLField(max_length=1024, blank=False, null=False)
    slug = models.SlugField(unique=True, blank=False, null=False)
    shortened_url = models.URLField(max_length=32, blank=False, null=False)

    def __str__(self):
        return self.shortened_url
