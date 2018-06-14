from rest_framework import serializers

from parking_project.offer.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
