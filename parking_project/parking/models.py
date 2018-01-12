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
                            help_text=('The request type'), blank=True)
    requestedAt = models.CharField(max_length=128, verbose_name=('Requested at'),
                            help_text=('Requested at'), blank=True)
    period = models.CharField(max_length=128, verbose_name=('period'),
                            help_text=('period'), blank=True)
    requestedFor = models.CharField(max_length=128, verbose_name=('Requested for'),
                            help_text=('requested for'), blank=True)
    createdBy = models.CharField(max_length=128, verbose_name=('created by'),
                            help_text=('created by'), blank=True)
    requestedFrom = models.CharField(max_length=128, verbose_name=('Request from'),
                            help_text=('Request from'), blank=True)
    reservationRequestedAt = models.CharField(max_length=128, verbose_name=('rezervation requested at'),
                                     help_text=('The request type'), blank=True)
    rentalRequestedAt = models.CharField(max_length=128, verbose_name=('rental requested at'),
                                 help_text=('rental requested at '), blank=True)
    parkingNo = models.IntegerField(verbose_name='parking number', blank=True, null=True)
    parking = models.ForeignKey('Parking', verbose_name='Parking', related_name='requests', default=1, blank=True)


class RequestType(models.Model):
    type = models.CharField(max_length=128, verbose_name=('Request type'),
                            help_text=('The request type'))
    parking = models.ForeignKey('Parking', verbose_name='Parking', related_name='requestTypes', default=None)
