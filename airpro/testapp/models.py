from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=56)
    def __str__(self):
        return self.name

class Passenger(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_id=models.EmailField(unique=True)
    mobile_number=models.CharField(max_length=13)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    age=models.PositiveSmallIntegerField()
    gender=models.CharField(max_length=10,choices=(('Male','Male'),('Female','Female')))


