from django.db import models
from extended_choices import Choices


class Offer(models.Model):
    STATUS_TYPE = Choices(
        ('AVAILABLE', 1, 'Available'),
        ('UNAVAILABLE', 2, 'UNAVAILABLE'),
    )
    start_date = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    creation_date = models.DateTimeField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_TYPE, verbose_name='status',
                                              default=STATUS_TYPE.AVAILABLE)
    creator = models.ForeignKey('account.Account', help_text='The user which created the offer')



