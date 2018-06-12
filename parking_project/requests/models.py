from django.db import models
from extended_choices import Choices


class Request(models.Model):
    """
    Request model
    """
    REQUEST_TYPES = Choices(
        ('ASK_FOR_SUBSCRIPTION', 1, 'Ask for subscription'),
        ('REQUEST_OFFER', 2, 'Request an offer')
    )

    REQUEST_STATUS = Choices(
        ('PENDING', 1, 'Pending'),
        ('ACCEPTED', 2, 'Accepted'),
        ('REJECTED', 3, 'Rejected')
    )

    request_type = models.PositiveSmallIntegerField(choices=REQUEST_TYPES, verbose_name='request type',
                                                    help_text='The type of request')

    status = models.PositiveSmallIntegerField(choices=REQUEST_STATUS, verbose_name='status',
                                              default=REQUEST_STATUS.PENDING)
    offer = models.ForeignKey('offer.Offer', related_name='requests')
    creator = models.ForeignKey('account.Account', related_name='own_requests')
    was_viewed = models.BooleanField(default=False)
