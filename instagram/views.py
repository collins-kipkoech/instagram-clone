from django.shortcuts import render,redirect
from .models import Image
from .forms import ImageForm
from cloudinary.forms import cl_init_js_callbacks




# Create your views here.
def index(request):
    posts = Image.objects.all()
    return render(request,'instagram/index.html',{'posts':posts})


def uploadImage(request):
    form = ImageForm()
    if request.method == 'POST':
        
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request,'instagram/upload.html',{'form':form})

def deleteImage(request,pk):
    post = Image.objects.get(id=pk)
    
    return render(request,'instagram/delete.html',{'post':post})



    
    
