from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from authentications.forms import RegistrationFrom


def register(request):
    if request.method == "POST":
        
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User created successfully")
            messages.error(request,form.errors)
            return redirect('registration')
           
  
    else: 
        form = RRegistrationFrom()
        context = {
            "form": form
        }
    return render(request,"registation.html",context)
        
  