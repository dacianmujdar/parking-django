from django.db import models
from extended_choices import Choices


class Request(models.Model):
    """
    Request model
    """
    REQUEST_STATUS = Choices(
        ('PENDING', 1, 'Pending'),
        ('ACCEPTED', 2, 'Accepted'),
        ('REJECTED', 3, 'Rejected')
    )
    status = models.PositiveSmallIntegerField(choices=REQUEST_STATUS, verbose_name='status',
                                              default=REQUEST_STATUS.PENDING)
    offer = models.ForeignKey('offer.Offer', related_name='requests')
    creator = models.ForeignKey('account.Account', related_name='own_requests')
    was_viewed = models.BooleanField(default=False)

    def __str__(self):
        return "Request: creator - {}, {}".format(self.creator, self.offer)
