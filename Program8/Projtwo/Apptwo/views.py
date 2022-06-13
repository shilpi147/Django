from django.shortcuts import render

# Create your views here.
def sample(request):

    return render(request,'sample.html')

def first(request):

    return render(request,'first.html')

