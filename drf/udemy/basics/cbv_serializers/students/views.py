import django.http
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

# CBV ModelViewSets

class StudentPagination(LimitOffsetPagination):
    default_limit = 3

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination
    # filter_backends = [DjangoFilterBackend]
    # exact matches filter
    # filterset_fields = ['name', 'score']

    filter_backends = [filters.SearchFilter]
    # through all fields 'contains' filter
    # search_fields = ['name', 'score']

    # ^ startswith filter
    # search_fields = ['^name', 'score']

    # = exact matches filter
    # search_fields = ['=name', 'score']

    # @ full-text filter (posgres only)
    # search_fields = ['@name', 'score']

    # $ regex filter
    # search_fields = ['$name', 'score']

    filter_backends.append(filters.OrderingFilter)
    ordering_fields = ['name', 'score']
    # for default ordering
    ordering = ['-score']

    # custom filter
    # def get_queryset(self):
    #     queryset = Student.objects.all()
    #     name = self.request.query_params.get('name')
    #     score = self.request.query_params.get('score')
    #     if name:
    #         queryset = queryset.filter(name__contains=name)
    #     if score:
    #         queryset = queryset.filter(score=score)
    #     return queryset

    permission_classes = (IsAuthenticated,)


"""
# CBV generics

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

"""

"""
# CBV mixins + GenericAPIView

class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

"""

"""
# CBV APIView

class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise django.http.Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(instance=student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
