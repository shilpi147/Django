from django.shortcuts import render

# Create your views here.

def link1(request):

    return render(request,'link1.html')


def link2(request):

    name = request.POST.get('username')
    age=request.POST.get('age')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    email = request.POST.get('mail')


    context = {'username':name , 'age':age ,'address':address,'phone':phone , 'email':email }

    return render(request,'link2.html',context)

def test1(request):
    return render(request,'test1.html')

def test2(request):
    return render(request,'test2.html')





