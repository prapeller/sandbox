from django.shortcuts import render
from rest_framework import decorators, status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


@decorators.api_view(['GET', 'POST'])
def users_list(request):
    """get/post for list User objs"""
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(['GET', 'PUT', 'DELETE'])
def users_details(request, pk):
    """get/put/delete for particular User object"""
    obj = User.objects.filter(pk=pk)
    if not obj:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(obj.first())
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)