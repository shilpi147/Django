from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    phone=models.IntegerField()

class Student(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    state=models.CharField(max_length=100)
