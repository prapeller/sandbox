from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from todo.models import Project, Todo
from todo.serializers import ProjectSerializer, TodoSerializer


class TenLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = TenLimitOffsetPagination

    def get_queryset(self):
        if self.request.query_params.get('name'):
            return Project.objects.filter(name__contains=self.request.query_params.get('name'))
        return Project.objects.all()


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = TenLimitOffsetPagination

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
