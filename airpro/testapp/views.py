from django.shortcuts import render
from .serializers import Booking_serializer
from testapp.models import Booking
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# class Booking_Listview(APIView):
#
#     def get(self,request,*args,**kwargs):
#         queryset=Booking.objects.all()
#         serializer=Booking_serializer(queryset,many=True)
#
#         return Response(serializer.data)
#     def post(self, request, *args, **kwargs):
#         serializer = Booking(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk, *args, **kwargs):
#         qs = Booking.objects.get(pk=pk)
#         serializer = Booking(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, *args, **kwargs):
#         qs = Booking.objects.get(pk=pk)
#         qs.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class BookingListView(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        data = []

        for booking in bookings:
            booking_data = {
                'id': booking.id,
                'passenger_name': booking.passenger.first_name,
                'source_name': booking.source.name,
                'destination_name': booking.destination.name,
                'date': booking.date
            }
            data.append(booking_data)

        return Response(data)