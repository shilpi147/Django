from django.shortcuts import render

# Create your views here.
from . models import Employee
from . models import Student

def login(request):

    return render(request,'login.html')


def insert(request):

    if(request.method=="POST"):
        name=request.POST.get('name')

        username = request.POST.get('username')

        password = request.POST.get('password')

        age = request.POST.get('age')

        address = request.POST.get('address')

        phone=request.POST.get('phone')

        obj = Employee() 

        obj.name = name

        obj.username=username

        obj.password = password

        obj.age = age

        obj.address = address

        obj.phone=phone

        obj.save()

        return render(request,'insert.html')

    else:

        return render(request,'login.html')

def student(request):
    return render (request,'student.html')

def studentinfo(request):
    name=request.POST.get('name')
    course=request.POST.get('course')
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    state=request.POST.get('state')

    obj=Student()
    obj.name=name
    obj.course=course
    obj.age=age
    obj.gender=gender
    obj.state=state
    obj.save()

    return render(request,'studentinfo.html')
