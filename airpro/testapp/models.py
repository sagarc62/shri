from django.db import models

# Create your models here.
class Passenger(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_id=models.EmailField(unique=True)
    mobile_number=models.IntegerField()
    age=models.PositiveSmallIntegerField()
    gender=models.CharField(max_length=10,choices=(('Male','Male'),('Female','Female')))