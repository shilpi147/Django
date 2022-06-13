from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sum(request):
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    return HttpResponse(a+b)
