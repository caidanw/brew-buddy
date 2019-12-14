from django.db import models


class StateCapital(models.Model):
    name = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    lat = models.FloatField()
    long = models.FloatField()
