from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from parking_project.parking.models import Parking, Request
from parking_project.parking.serializers import ParkingSerializer, RequestSerializer


def detail(request):
    return HttpResponse("Yo")


class ParkingList(GenericAPIView, ListModelMixin):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RequestDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        This view returns the list of applications
        belonging to an application package
        """
        request_id = self.kwargs['pk']
        return Request.objects.filter(id=request_id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CreateRequest(GenericAPIView, CreateModelMixin):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
