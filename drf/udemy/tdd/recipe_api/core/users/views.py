from django.contrib.auth import get_user_model

from rest_framework import mixins, viewsets, generics

from users.serializers import UserSerializer


class ListCreateUserView(generics.ListCreateAPIView):
    """Create a new user in the system"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    """Create a new user in the system"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
