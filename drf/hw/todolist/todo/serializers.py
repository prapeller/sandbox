from rest_framework.serializers import ModelSerializer, StringRelatedField
from todo.models import Project, Todo


class ProjectSerializer(ModelSerializer):
    users = StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = '__all__'


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
