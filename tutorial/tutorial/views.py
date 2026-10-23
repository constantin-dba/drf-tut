from django.contrib.auth.models import User
from rest_framework import generics
from tutorial.serializers import UserListSerializer, UserDetailSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
