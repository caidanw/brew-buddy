from django.db import models


class Brewery(models.Model):
    name = models.CharField(max_length=100)
    brewery_type = models.CharField(max_length=20)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
    phone = models.CharField(max_length=12, blank=True)
    website_url = models.URLField(blank=True)
    updated_at = models.DateTimeField()
