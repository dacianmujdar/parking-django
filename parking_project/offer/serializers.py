from rest_framework import serializers

from parking_project.account.serializers import AccountSerializer
from parking_project.offer.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    parking_space_code = serializers.SerializerMethodField()
    creator = AccountSerializer()

    class Meta:
        model = Offer

    def get_parking_space_code(self, offer):
        return offer.parking_space.code


class CreateOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
