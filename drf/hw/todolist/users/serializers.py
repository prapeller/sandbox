from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from users.models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'url']