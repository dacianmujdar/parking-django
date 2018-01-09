from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Parking(models.Model):
    """
    Parking model
    """


class Account(models.Model):
    """
    User account model
    """
    user = models.OneToOneField(User, related_name='profile')

    def __unicode__(self):
        return self.user.username


class Request(models.Model):
    """
    Request model
    """
    type = models.CharField(max_length=128, verbose_name=('Request type'),
                            help_text=('The request type'))
    requestedAt = models.CharField(max_length=128, verbose_name=('Requested at'),
                            help_text=('Requested at'))
    period = models.CharField(max_length=128, verbose_name=('period'),
                            help_text=('period'))
    requestedFor = models.CharField(max_length=128, verbose_name=('Requested for'),
                            help_text=('requested for'))
    createdBy = models.CharField(max_length=128, verbose_name=('created by'),
                            help_text=('created by'))
    requestedFrom = models.CharField(max_length=128, verbose_name=('Request from'),
                            help_text=('Request from'))
    reservationRequestedAt = models.CharField(max_length=128, verbose_name=('rezervation requested at'),
                                     help_text=('The request type'))
    rentalRequestedAt = models.CharField(max_length=128, verbose_name=('rental requested at'),
                                 help_text=('rental requested at '))
    parkingNo = models.IntegerField(verbose_name='parking number')
    parking = models.ForeignKey('Parking', verbose_name='Parking', related_name='requests', default=None)



class RequestType(models.Model):
    type = models.CharField(max_length=128, verbose_name=('Request type'),
                            help_text=('The request type'))
    parking = models.ForeignKey('Parking', verbose_name='Parking', related_name='requestTypes', default=None)
