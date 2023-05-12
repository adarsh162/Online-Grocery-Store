from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
def login(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect(login)
    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def index1  (request):
    if(request.method=="POST"):
       first_name=request.POST['first_name']
       last_name=request.POST['last_name']
       username=request.POST['username']
       password1=request.POST['password1']
       password2=request.POST['password2']
       email=request.POST['email']
       if password1==password2:
           if(User.objects.filter(username=username).exists()):
               messages.info(request,'Username is not available')
               return redirect('index1')
              # print('User Name is not available')
           elif(User.objects.filter(email=email).exists()):
                 messages.info(request,'Email id is already taken')
                 return redirect('index1')
               
           else:
               user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
               user.save()
               print('User created')
       else:
           messages.info(request,'Password not matching.')
           return redirect('index')
           
       return redirect('/')
    else:
        return render(request,'index1.html')
            
    
