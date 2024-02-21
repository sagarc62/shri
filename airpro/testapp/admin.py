from django.contrib import admin
from testapp.models import Passenger,City
# Register your models here.
class Passenger_Admin(admin.ModelAdmin):
    fields=['first_name','last_name','email_id','mobile_number','city','age','gender']

class City_Admin(admin.ModelAdmin):
    fields=['name']

admin.site.register(Passenger,Passenger_Admin)
admin.site.register(City,City_Admin)