from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """
    User account model
    """
    user = models.OneToOneField(User, related_name='profile')
    phone_no = models.CharField(max_length=15, blank=True, null=True)

    def __unicode__(self):
        return self.user.username
