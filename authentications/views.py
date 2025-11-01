from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login,logout
 

 
 




def register(request):
    if request.method == "POST":
        
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User created successfully")
            return redirect('registration')
        messages.error(request,"This user isn't created")
        return redirect('registration')
           
  
    else: 
        form = RegistrationForm()
    context = {
            "form": form
        }
    return render(request,"registation.html",context)


def login_view(request):
    if request.user.is_authenticated:
       return redirect ("student-list")

       
    if request.method =="POST":
       username = request.POST.get("username")
       password = request.POST.get("password")
       
       user = authenticate(request, username=username, password=password)
       
       if user is not None:
           login(request,user)
           return redirect("student-list")
       messages.error(request,"username or password isn't valid")
       return redirect("Log-in")
 
    return render(request,"login.html")


def sign_out(request):
    logout(request)
    return redirect("Log-in")
    


    