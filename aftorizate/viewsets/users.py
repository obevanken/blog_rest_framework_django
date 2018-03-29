from aftorizate.serializers import UserSerializer, PostUserSerializer
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import User


class UserViewSet(mixins.CreateModelMixin, GenericViewSet, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = PostUserSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
