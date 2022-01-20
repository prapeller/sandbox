import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from todo.models import Project, Todo
from todo.serializers import ProjectSerializer, TodoSerializer, ProjectSerializerV2


class TenLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    # serializer_class = ProjectSerializer
    pagination_class = TenLimitOffsetPagination

    def get_queryset(self):
        if self.request.query_params.get('name'):
            return Project.objects.filter(name__contains=self.request.query_params.get('name'))
        return Project.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ProjectSerializerV2
        return ProjectSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = TenLimitOffsetPagination

    def create(self, request, *args, **kwargs):
        todo = Todo.objects.create(creator=request.user)
        serializer = self.get_serializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        serializer=self.get_serializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
