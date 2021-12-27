from rest_framework import serializers
from core.models import TravelPoints, Passenger


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'first_name', 'last_name', 'travel_points']


class TravelPoint(serializers.ModelSerializer):
    class Meta:
        model = TravelPoints
        fields = ['city']
