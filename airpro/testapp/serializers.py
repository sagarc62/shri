from rest_framework import serializers
from testapp.models import Booking
class Booking_serializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'