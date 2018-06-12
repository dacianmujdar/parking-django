from rest_framework import serializers

from parking_project.parking.models import Parking
from parking_project.requests.serializers import RequestSerializer


class ParkingSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Parking
