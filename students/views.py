from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
# Create your views here.

def Student_list(request):
    
    students = Student.objects.all().order_by("-create_at")
    if students:
        context = {
            "data":students
        }
        return render(request,"Student_list.html",context)
    else:
        return HttpResponse("Not Available Data")
      



def add_student(request):
    if request.method == "POST":
        
      Name = request.POST.get("Name")
      Age = request.POST.get("Age")
      Course = request.POST.get("Course")
      
      print(Name,Age,Course)
      data = Student(Name=Name,Age=Age,Course=Course)
      data.save()
      print("data is saved successfully")
      return redirect("student-list")
    return render(request,"student_form.html")

def update_student(request,id):
    Change = Student.objects.get(id=id)
    
    if request.method == "POST":
        
      Name = request.POST.get("Name")
      Age = request.POST.get("Age")
      Course = request.POST.get("Course")
      
      
      
      Change.Name = Name
      Change.Age = Age
      Change.Course = Course
      Change.save()
      
      return redirect("student-list")
    
    context = {
        "id": Change.id,
        "Name": Change.Name,
        "Age": Change.Age,
        "Course": Change.Course,
    }
    return render(request,"student_update.html",context)
    


def delete_student(request,id):
    delete = Student.objects.get(id=id)
    
    delete.delete() 
    return redirect("student-list")
    

    

    
    

     

        

       

    



    