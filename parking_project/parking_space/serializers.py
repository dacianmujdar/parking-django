from rest_framework import serializers
from parking_project.parking_space.models import ParkingSpace


class ParkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpace
        fields = ('code', 'is_occupied', 'times_extended', 'start_date', 'expiration_date')
