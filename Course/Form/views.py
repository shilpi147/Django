
from django.shortcuts import render


from .models import Course

# Create your views here.
def Registration(request):
    return render(request,'Registration.html')

def Submit(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        email=request.POST.get('mail')
        qualification=request.POST.get('quali')
        address=request.POST.get('address')
        course=request.POST.get('course')
        alternateno=request.POST.get('alter')
        gender=request.POST.get('gender')
        source=request.POST.get('source')
        experience=request.POST.get('exp')
        plan=request.POST.get('plan')
        job=request.POST.get('job')
        batch=request.POST.get('batch')

        obj=Course()
        obj.name=name
        obj.age=age
        obj.phone=phone
        obj.email=email
        obj.qualification=qualification
        obj.address=address
        obj.course=course
        obj.alternateno=alternateno
        obj.gender=gender
        obj.source=source
        obj.experience=experience
        obj.plan=plan
        obj.job=job
        obj.batch=batch

        obj.save()

        return render(request,'Submit.html')