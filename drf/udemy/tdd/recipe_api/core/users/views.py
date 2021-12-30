from django.contrib.auth import get_user_model

from rest_framework import mixins, viewsets, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from users.serializers import UserSerializer, AuthTokenSerializer


class ListCreateUserView(generics.ListCreateAPIView):
    """Create a new user in the system"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    """Create a new user in the system"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
