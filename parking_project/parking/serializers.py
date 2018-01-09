from rest_framework import serializers

from parking_project.parking.models import Parking, Request, RequestType


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request


class RequestTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestType


class ParkingSerializer(serializers.ModelSerializer):
    requestTypes = RequestTypesSerializer(many=True)
    requests = RequestSerializer(many=True)

    class Meta:
        model = Parking

