from django.shortcuts import render
from rest_framework import mixins, generics, viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import User
from .serializers import UserSerializer


class UserModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer
