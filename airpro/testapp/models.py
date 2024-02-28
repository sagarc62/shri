from django.db import models
from django.utils import timezone
# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=56)
    def __str__(self):
        return str(self.name)

class Airport(models.Model):
    name=models.CharField(max_length=56)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} {self.city}'

class Passenger(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_id=models.EmailField(unique=True)
    mobile_number=models.CharField(max_length=13)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    age=models.PositiveSmallIntegerField()
    gender=models.CharField(max_length=10,choices=(('Male','Male'),('Female','Female')))
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# class Source_city(models.Model):
#     name=models.OneToOneField(City,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name
#
# class Destination_city(models.Model):
#     name=models.OneToOneField(City,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name

class Booking(models.Model):
    passenger=models.OneToOneField(Passenger,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    source=models.OneToOneField(Airport,related_name='source',on_delete=models.CASCADE)

    destination = models.OneToOneField(Airport,related_name='destination', on_delete=models.CASCADE)
    travel_class=models.CharField(max_length=10,choices=(('Premium','Premium'),('Economy','Economy')))
    def __str__(self):
        return self.passenger


