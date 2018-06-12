from rest_framework import mixins
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response

from django.db.models import Q

from parking_project.requests.models import Request
from parking_project.requests.serializers import RequestSerializer


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


class RequestView(GenericAPIView, CreateModelMixin, ListModelMixin):
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Request.objects.filter(creator=self.request.user.profile)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class InboxView(GenericAPIView, ListModelMixin):
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        account = self.request.user.profile
        # all requests made to user offers OR all requests created by the user with status ACCEPTED or REJECTED
        return Request.objects.filter(Q(offer__creator=account) | Q(creator=account, status_gt=1))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AcceptRequestView(GenericAPIView, CreateModelMixin):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request_id = self.kwargs['pk']
        request = Request.objects.get(id=request_id)
        offer = request.offer

        if offer.creator.user != self.request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # change all other requests to REJECTED
        for req in offer.requests.all():
            req.status = Request.REQUEST_STATUS.REJECTED
            req.save()

        request.status = Request.REQUEST_STATUS.ACCEPTED
        request.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class RejectRequestView(GenericAPIView, CreateModelMixin):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request_id = self.kwargs['pk']
        request = Request.objects.get(id=request_id)
        offer = request.offer

        if offer.creator.user != self.request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)

        request.status = Request.REQUEST_STATUS.REJECTED
        request.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MarkAsViewedView(GenericAPIView, CreateModelMixin):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request_id = self.kwargs['pk']
        request = Request.objects.get(id=request_id)

        request.was_viewed = True
        request.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
