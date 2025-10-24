from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
# Create your views here.
from .forms import StudentForm
from django.contrib import messages

def Student_list(request):
    
    students = Student.objects.all().order_by("-create_at")
    if students:
        context = {
            "data":students
        }
        return render(request,"Student_list.html",context)
    else:
        return HttpResponse("Not Available Data")
      



def create(request):
    if request.method == "POST":
        
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Add student Successfully")
            return redirect("add-student")
        messages.error(request,"error this student is not added")
    #   return redirect("add-student")
  
    else: 
        form = StudentForm()
        context = {
            "form": form
        }
    return render(request,"student_form.html",context)
        
  
  
  
def update_student(request,id):
    try:
        Change = Student.objects.get(id=id)
    except:
        return HttpResponse(f"Id {id} is not founded") 
    
    
    if request.method == "POST":
        
        form = StudentForm(request.POST,instance=Change)
        if form.is_valid():
            form.save()
            messages.success(request, " student Updated Successfully")
            return redirect("student-list")
        messages.error(request,"error this student is not updated")
    
  
    else: 
        form = StudentForm(instance=Change)
        context = {
            "form": form,
            "id": id
        }
    return render(request,"student_update.html",context)
    

def delete_student(request,id):
        try:
            delete = Student.objects.get(id=id)
        except:
            return HttpResponse(f"Id {id} is not found")
            
        delete.delete()   
        messages.success(request,"This student is successfully deleted")
        return redirect("student-list")
        

    

    
    

     

        

       

    



    