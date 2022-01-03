from rest_framework import mixins, generics, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from .models import User
from .serializers import UserSerializer

class TwentyOffsetPagination(LimitOffsetPagination):
    default_limit = 20

class UserModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = TwentyOffsetPagination
