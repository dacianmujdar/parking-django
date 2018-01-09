from rest_framework import serializers

from parking_project.parking.models import Parking


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
