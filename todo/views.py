from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def home(request):
    return HttpResponse("Welcome to my Blog")



def show_items(request):
    blogs = Blog.objects.all()
    result =""
    for blog in blogs:
        result += f'<h1>{blog.title}</h1>'
        result += f'<h3>{blog.description}</h3>'
    return HttpResponse(result)


def index(request):
    todo_list = Blog.objects.filter(pk=2).order_by("-creat_at")
      
    for q in todo_list:
        print("title", q.title)
        print("description", q.description)
        print("creat_at",q.creat_at)
        
    output = "".join ([f'{q.title} <br> {q.description} <br> {q.creat_at}'  for q in todo_list])
    return HttpResponse(output)

    
def about(request):
    return render(request, "about.html")


def get_all(request):
    print("request",request)
    
    todo_list = Blog.objects.all().order_by("-creat_at")
    context = {
        "data": todo_list,
        "html_title" : "Items page"
    }
    return render(request, "home.html", context)


def create(request):
    
    if request.method == "POST":
        
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Add Items successfully")
            return redirect("add-items")
        
        messages.error(request, "error adding items")
        return redirect("add-items")

        #  title = request.POST.get("name")
        #  describtion = request.POST.get("describtion")
         
        #  print(title, describtion)
         
        #  data = Todo(title=title, describtion=describtion)
        #  data.save()
         
        #  print("data is saved successfully")
         
        # #  Todo.objects.create(title=title, describtion=describtion)
         
       
    
    else:
        
        form = TodoForm()
        context = {
            "form": form
        }
    
        return render(request, "add_items.html", context)
    
    
    

def update(request, id):
    
    try:

     todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)
        return HttpResponse(f"{id} {e}")
      
    if request.method =="POST":
        
        form = TodoForm(request.POST, instance=todo)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Items sucessfully updated")
            
            return redirect("update", id=todo.id)
        
        messages.error("error updating items")
        return redirect("update", id=todo.id)
   

    form = TodoForm(instance=todo)
    
    context = {
    "id": todo.id,
    "form": form
    }

    return render(request, "edit_items.html", context)
    

    

def delete(request, id):
    try:

     todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)
        return HttpResponse(f"{id} {e}")

    todo.delete()
    messages.success(request, "Items deleted succesfully")
    return redirect("get-all")
    