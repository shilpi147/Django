from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse ("Hey ! This is My first Django Project !")
def second(request):
    return HttpResponse("Hello ! This is Shilpika")
