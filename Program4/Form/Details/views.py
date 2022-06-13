from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'sample.html')

def second(request):
    return render(request,'color.html')
