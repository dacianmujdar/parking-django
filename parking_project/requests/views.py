from rest_framework import mixins
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework import views

from django.db.models import Q

from parking_project.offer.models import Offer
from parking_project.requests.models import Request
from parking_project.requests.serializers import RequestSerializer


class RequestDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """
        This view returns the list of applications
        belonging to an application package
        """
        request_id = int(self.kwargs['pk'])
        return get_object_or_404(Request, id=request_id, creator=self.request.user.profile)

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
        return Request.objects.filter(creator=self.request.user.profile).order_by('-created')

    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        if 'offer' not in request.data:
            return Response("Please provide the field offer", status=400)

        offer = get_object_or_404(Offer, id=int(request.data['offer']))
        request = Request.objects.create(creator=self.request.user.profile, offer=offer)
        return Response(RequestSerializer(instance=request).data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class InboxView(GenericAPIView, ListModelMixin):
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        account = self.request.user.profile
        # all requests made to user offers OR all requests created by the user with status ACCEPTED or REJECTED
        return Request.objects.filter(Q(offer__creator=account) | Q(creator=account, status__gt=1)).order_by('-modified')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AcceptRequestView(views.APIView):
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


class RejectRequestView(views.APIView):
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


class MarkAsViewedView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request_id = self.kwargs['pk']
        request = Request.objects.get(id=request_id)

        request.was_viewed = True
        request.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
