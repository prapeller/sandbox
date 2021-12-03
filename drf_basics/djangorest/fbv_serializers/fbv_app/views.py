from django.shortcuts import render
from fbv_app import models, serializers
from rest_framework import response, status


def student_list(request):
    """processing get/post methods for list of Student objects"""

    if request.method == 'GET':
        students = models.Student.objects.all()
        serializer = serializers.StudentSerializer(students, many=True)
        return response.Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)


def student_detail(request, pk):
    """processing get/put/patch methods for Student object"""
    try:
        student = models.Student.objects.get(pk=pk)
    except models.Student.DoesNotExist:
        return response.Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.StudentSerializer(student)
        return response.Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
