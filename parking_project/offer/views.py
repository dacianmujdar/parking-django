from channels_api.mixins import ListModelMixin
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin

from parking_project.offer.models import Offer
from parking_project.offer.serializers import OfferSerializer


class OffersView(GenericAPIView, CreateModelMixin, ListModelMixin, DestroyModelMixin):
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Offer.objects.filter(creator=self.request.user.profile)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)
