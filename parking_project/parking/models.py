from __future__ import unicode_literals

from django.db import models


class Parking(models.Model):
    """
    Parking model
    """
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=300)

    def __str__(self):
        return self.name
