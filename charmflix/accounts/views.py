from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UpdateProfileForm
from .models import Customer
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1!=password2:
            return redirect('register')

        if User.objects.filter(username=username).exists():
            return redirect('register')

        if User.objects.filter(email=email).exists():
            return redirect('register')

        user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
        customer = Customer.objects.create(user=user)
        customer.save()
        user.save()
		
        return redirect('login')

        
    
    return render(request,"autho/register.html")
    
    


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password1']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        
        return redirect('login')
    
    return render(request,'autho/login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required(login_url='/accounts/login/')
def myprofile(request):   

    if request.method=="POST":
        user=request.user
        user.email=request.POST['email']
        user.username=request.POST['username']
        customerform=UpdateProfileForm(request.POST, request.FILES, instance=request.user.customer)
        
        if customerform.is_valid():
            customerform.save()
            user.save()
            return redirect('myprofile')


    customerform=UpdateProfileForm(instance=request.user.customer)

    context={
        'customer':request.user.customer,
        'customerform':customerform,
    }
    
    return render(request,"autho/myprofile.html",context)
