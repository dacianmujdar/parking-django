from rest_framework import mixins
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from parking_project.parking.models import Parking
from parking_project.parking.serializers import ParkingSerializer
from parking_project.parking_space_detector.parking_detector import refresh_frames


class ParkingList(GenericAPIView, ListModelMixin):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        refresh_frames()
        return self.list(request, *args, **kwargs)
