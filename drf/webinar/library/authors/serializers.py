from rest_framework.serializers import Serializer, ModelSerializer, CharField, IntegerField, \
    ValidationError, StringRelatedField

from .models import Author, Bio, Book


# class AuthorSerializer(HyperlinkedModelSerializer):
class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        # fields = ['id', 'first_name', 'last_name', 'birth_year', 'url']
        fields = '__all__'


class AuthorSerializer(Serializer):
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    birth_year = IntegerField()

    def create(self, validated_data):
        author = Author(**validated_data)
        author.save()
        return author

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birth_year = validated_data.get('birth_year', instance.birth_year)
        instance.save()
        return instance

    def validate_birth_year(self, value):
        if value < 1000:
            raise ValidationError('value cant be less then 1000')
        return value

    def validate(self, attrs):
        if (attrs['last_name'] == 'Dostoevsky') and (attrs['birth_year'] != 1821):
            raise ValidationError('Birth year of Dostoevsky must be 1821')
        return attrs


class BioSerializer(Serializer):
    text = CharField(max_length=64)
    author = AuthorSerializer()


class BookSerializer(Serializer):
    name = CharField(max_length=64)
    authors = AuthorSerializer(many=True)


class BioModelSerializer(ModelSerializer):
    # author = AuthorModelSerializer()
    # author = StringRelatedField()

    class Meta:
        model = Bio
        fields = '__all__'

class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

