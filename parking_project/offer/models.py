from django.db import models
from extended_choices import Choices


class Offer(models.Model):
    STATUS_TYPE = Choices(
        ('AVAILABLE', 1, 'Available'),
        ('UNAVAILABLE', 2, 'Unavailable'),
        ('DELETED', 3, 'Deleted by the creator'),
    )
    start_date = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    creation_date = models.DateTimeField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_TYPE, verbose_name='status',
                                              default=STATUS_TYPE.AVAILABLE)
    creator = models.ForeignKey('account.Account', related_name='own_offers', help_text='The user which created the offer')
    parking_space = models.ForeignKey('parking_space.ParkingSpace', related_name='offers', null=True, blank=True)

    def __str__(self):
        if self.start_date and self.expiration_date:
            return "Offer: period - {} : {}, creator - {}, {}".format(self.start_date.date(), self.expiration_date.date(),
                                                                      self.creator, self.parking_space)
        return "Offer: creator - {}, {}".format(self.creator, self.parking_space)
