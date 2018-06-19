from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin

from parking_project.offer.models import Offer
from parking_project.offer.serializers import OfferSerializer, CreateOfferSerializer
from parking_project.requests.models import Request


class OffersView(GenericAPIView, CreateModelMixin, ListModelMixin):
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Offer.objects.filter(creator=self.request.user.profile, status__lte=2)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = CreateOfferSerializer()
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OfferDetail(DestroyModelMixin, GenericAPIView):
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        offer_id = self.kwargs['pk']
        return get_object_or_404(Offer, id=offer_id, creator=self.request.user.profile)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if hasattr(instance, 'requests'):
            for request in instance.requests.all():
                request.status = Request.REQUEST_STATUS.REJECTED
                request.save()
        instance.status = Offer.STATUS_TYPE.DELETED
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
