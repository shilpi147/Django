from django.shortcuts import render

# Create your views here.
def abc(request):
    return render(request,'abc.html')

def xyz(request):
    return render(request,'xyz.html')

