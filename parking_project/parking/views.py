from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from parking_project.parking.models import Parking
from parking_project.parking.serializers import ParkingSerializer


class ParkingList(GenericAPIView, ListModelMixin):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
