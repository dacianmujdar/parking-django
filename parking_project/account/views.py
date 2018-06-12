from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.generics import GenericAPIView

from parking_project.account.serializers import AccountSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile
