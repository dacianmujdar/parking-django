from rest_framework import serializers

from parking_project.account.serializers import AccountSerializer
from parking_project.offer.serializers import OfferSerializer
from parking_project.requests.models import Request


class RequestSerializer(serializers.ModelSerializer):
    offer = OfferSerializer(read_only=True)
    creator = AccountSerializer(read_only=True)

    class Meta:
        model = Request
        exclude_fields = ('created',)

