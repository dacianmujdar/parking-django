from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Camera(models.Model):
    url = models.TextField(help_text="The video stream url")
    parking = models.ForeignKey('parking.Parking', help_text='The parking where the camera belongs')

