from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created Successfully')
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'users/register.html',{'form':form})


def profile(request):
    return render(request,'users/profile.html')
