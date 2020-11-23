from django.shortcuts import render,redirect
from .models import Image
from .forms import ImageForm
from cloudinary.forms import cl_init_js_callbacks
from django.contrib import messages




# Create your views here.
def index(request):
    posts = Image.objects.all()
    return render(request,'instagram/index.html',{'posts':posts})


def uploadImage(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, f'your photo has been uploaded successfully')
            return redirect('index')


    form = ImageForm()
    ctx = {'form':form}

    return render(request,'instagram/upload.html',ctx)





    
    
