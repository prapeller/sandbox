from django.contrib.auth import get_user_model

from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, StringRelatedField, DateTimeField, DateField

from todo.models import Project, Todo


class ProjectSerializer(ModelSerializer):
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectSerializerV2(ModelSerializer):
    users = PrimaryKeyRelatedField(many=True, queryset=get_user_model().objects.all())

    class Meta:
        model = Project
        fields = '__all__'


class TodoSerializer(ModelSerializer):
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)
    class Meta:
        model = Todo
        fields = ('created_at', 'updated_at', 'id', 'text', 'is_active', 'project')
