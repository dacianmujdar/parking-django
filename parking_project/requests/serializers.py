from rest_framework import serializers

from parking_project.requests.models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request

