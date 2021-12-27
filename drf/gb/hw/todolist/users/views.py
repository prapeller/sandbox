import rest_framework.permissions
from django.shortcuts import render
from rest_framework import mixins, generics, viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .models import User
from .serializers import UserSerializer


class UserModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer
