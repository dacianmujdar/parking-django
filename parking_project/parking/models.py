from __future__ import unicode_literals

from django.db import models


class Parking(models.Model):
    """
    Parking model
    """
    name = models.CharField(max_length=128, verbose_name=('Parking name'),
                            help_text=('The Parking name'))
