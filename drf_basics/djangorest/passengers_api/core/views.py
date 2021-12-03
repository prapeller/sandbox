from rest_framework import status, decorators
from rest_framework.response import Response
from core.serializers import PassengerSerializer
from core import models, serializers


@decorators.api_view(['GET', 'POST'])
def passengers_list(request):
    """processing get/post for list of Passenger objects"""

    if request.method == 'GET':
        query_set = models.Passenger.objects.all()
        ser = PassengerSerializer(query_set, many=True)
        return Response(ser.data)

    elif request.method == 'POST':
        ser = PassengerSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(['GET', 'PUT', 'DELETE'])
def passengers_details(request, pk):
    """processing get/put/delete for particular Passenger object"""
    try:
        query_obj = models.Passenger.objects.get(pk=pk)
    except models.Passenger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = PassengerSerializer(query_obj)
        return Response(ser.data)

    elif request.method == 'PUT':
        ser = PassengerSerializer(query_obj, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        query_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
