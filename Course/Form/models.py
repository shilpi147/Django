from django.db import models
from numpy import source

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)
    qualification=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    alternateno=models.IntegerField()
    gender=models.CharField(max_length=10)
    source=models.CharField(max_length=10)
    experience=models.CharField(max_length=10)
    plan=models.CharField(max_length=10)
    job=models.CharField(max_length=10)
    batch=models.CharField(max_length=10)
    

    
