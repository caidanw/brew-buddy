from django.db import models


class Brewery(models.Model):
    name = models.CharField(max_length=100, null=True)
    brewery_type = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=200, null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    updated_at = models.DateTimeField()
