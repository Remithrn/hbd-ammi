from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')

def cake(request):
    return render(request,'index.html')

def wish(request):
    return render(request,'bubbles.html')