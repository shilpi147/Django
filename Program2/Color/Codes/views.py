from django.shortcuts import render

# Create your views here.
def work(request):
    return render(request,'task.html')
def hello(request):
    return render(request,'first.html')
def home(request):
    return render(request,'home.html')
def table(request):
    return render(request,'table.html')
def user(request):
    return render(request,'user.html')
def odd(request):
    return render(request,'odd.html')





