from rest_framework import serializers

from parking_project.parking.models import Parking
from parking_project.requests.serializers import RequestSerializer


class ParkingSerializer(serializers.ModelSerializer):
    requests = RequestSerializer(many=True)
    is_administrator = serializers.SerializerMethodField()

    class Meta:
        model = Parking

    def get_is_administrator(self, parking):
        return self.context['request'].user.is_staff

