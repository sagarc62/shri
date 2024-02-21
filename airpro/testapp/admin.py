from django.contrib import admin
from testapp.models import Passenger
# Register your models here.
class Passenger_Admin(admin.ModelAdmin):
    fields=['first_name','last_name','email_id','mobile_number','age','gender']


admin.site.register(Passenger,Passenger_Admin)