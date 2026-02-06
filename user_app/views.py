from django.shortcuts import render,redirect

from django.views.generic import View

from django.core.mail import send_mail

from user_app.forms import *

from user_app.models import *

from user_task.models import *

from django.contrib.auth import authenticate,login,logout

# Create your views here.

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.core.mail import send_mail
from user_app.forms import UserRegister  # assuming your form is named like this

class RegisterView(View):
    
    def get(self, request):
        form = UserRegister()
        return render(request, 'signup.html', {"form": form})
    
    def post(self, request):
        form = UserRegister(request.POST)

        if form.is_valid():
            # Save user using form data
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            # Send welcome email
            send_mail(
                subject="Hello from TODO",
                message="Welcome to TODO!",
                from_email="sobyfrancic90@gmail.com",
                recipient_list=[form.cleaned_data['email']],
                fail_silently=True
            )

            return redirect("signin")
        
        # If form is invalid, re-render the page with errors
        return render(request, 'signup.html', {"form": form})

    
class Signin(View):
    
    def get(self,request):
        
        return render(request,'signin.html')
    
    def post(self,request):
        
        username = request.POST.get('username')
        
        password = request.POST.get('password')
        
        user = authenticate(request,username = username,password = password)
        
        if user:
            
            login(request,user)
            
            return redirect("home")
        
        return redirect("signin")
    
class LogoutView(View):
    
    def get(self,request):
        
        logout(request)
        
        return redirect("home")
    
class BaseView(View):
    def get(self,request):
        
        if request.user.is_authenticated:
        
            task = Task.objects.filter(user = request.user)
        
            return render(request,"home.html",{"task":task})
        return render(request,"home.html")
        
    

    
