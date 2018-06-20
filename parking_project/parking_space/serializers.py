from rest_framework import serializers

from parking_project.account.serializers import AccountSerializer
from parking_project.parking_space.models import ParkingSpace


class ParkingSpaceSerializer(serializers.ModelSerializer):
    allocated_to = AccountSerializer(read_only=True)

    class Meta:
        model = ParkingSpace
        fields = ('id', 'code', 'is_occupied', 'times_extended', 'start_date', 'expiration_date', 'allocated_to')
