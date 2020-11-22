from django.shortcuts import render
from .models import Image




# Create your views here.
def index(request):
    posts = Image.objects.all()
    return render(request,'instagram/index.html',{'posts':posts})


def uploadImage(request):
    return render(request,'instagram/upload.html')



    
    
