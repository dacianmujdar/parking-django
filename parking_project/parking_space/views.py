from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from parking_project.parking_space.models import ParkingSpace
from parking_project.parking_space.serializers import ParkingSpaceSerializer


class ParkingSpacesList(GenericAPIView, ListModelMixin):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return ParkingSpace.objects.filter(parking=self.kwargs['parking_id'])

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

