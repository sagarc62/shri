from django.contrib import admin
from testapp.models import Passenger,City,Airport,Booking
# Register your models here.
class Passenger_Admin(admin.ModelAdmin):
    fields=['first_name','last_name','email_id','mobile_number','city','age','gender']

class City_Admin(admin.ModelAdmin):
    fields=['name']

class Airport_admin(admin.ModelAdmin):
    fields=['name','city']

# class Source_admin(admin.ModelAdmin):
#     fields=['name']
#
# class Destination_admin(admin.ModelAdmin):
#     fields=['name']

class Booking_admin(admin.ModelAdmin):
    fields=['passenger','date','source','destination','travel_class']

admin.site.register(Passenger,Passenger_Admin)
admin.site.register(City,City_Admin)
admin.site.register(Airport,Airport_admin)
# admin.site.register(Source_city,Source_admin)
# admin.site.register(Destination_city,Destination_admin)
admin.site.register(Booking,Booking_admin)