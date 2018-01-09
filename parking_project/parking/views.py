from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from parking_project.parking.models import Parking
from parking_project.parking.serializers import ParkingSerializer


def detail(request):
    return HttpResponse("Yo")


class ParkingList(GenericAPIView, ListModelMixin):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    permission_class = permissions.IsAuthenticated

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)