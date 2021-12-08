from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Author


# class AuthorSerializer(HyperlinkedModelSerializer):
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        # fields = ['id', 'first_name', 'last_name', 'birth_year', 'url']
        fields = '__all__'