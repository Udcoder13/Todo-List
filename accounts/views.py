from django.shortcuts import render
from.forms import UserForm,UserLoginForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from Assign.views import home
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def registration(request):
    if request.method=='POST':
        user=UserForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('home')
        else:
            return render(request,'register.html',{'form':user})
    else:
     user=UserForm()
     return render(request,'register.html',{'form':user})

def loginView(request):
    loginf=UserLoginForm(request,data=request.POST)
    if request.method == 'POST':
        if loginf.is_valid():
         username=loginf.cleaned_data['username']
         password=loginf.cleaned_data['password']
         user=authenticate(username=username,password=password)
         if user is not None:
            login(request,user)
            return redirect('home')
              

    else:
        return render(request,'login.html',{'form':loginf})
    return render(request,'login.html',{'form':loginf})

@login_required
def logoutView(request):
    logout(request)
    return redirect('home')


