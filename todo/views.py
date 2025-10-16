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
        result += f'<h2>{blog.author}</h2>'
        result += f'<h3>{blog.content}</h3>'
    return HttpResponse(result)




def create(request):
    if request.method == "POST":
    
     title = request.POST.get("title")
     description = request.POST.get("description")
    
     print(title, description)
     data = Blog (title=title,description=description)
     data.save()
    
     print("data is saved successfully")
     return redirect("get-all")

    return render(request,"add_items.html") 


   
   
   
   

def get_all(request):

    
    # todo_list = Blog.objects.all()
    # title = todo_list['title']
    # description = todo_list['description']
    
    # print("efjsdlkfs --- ", title, description)
    
    # if todo_list:
    #     print(todo_list)
        
    #     for q in todo_list:
    #         print("id",q.id)
    #         print("title",q.title)
    #         print("description",q.description)
    #     output = ",".join([q.description for q in todo_list])
    #     return HttpResponse(output)   
    # else:
    #     return HttpResponse(f"Not Evailable data") 
    
    
    def create(request):
        Blog.objects.create()
    
    def update(request,id,title,description):
         todo = Blog.objects.get(id=id)
         todo.title = title
         todo.description = description
         todo.save()
         return HttpResponse(f"{id} was deleted successfully") 
     
     
    def update(request):
        return HttpResponse("this is update page")  
    
    return render(request, "add_items.html", {"blog": todo_list})
        
    
    
def see_all(req):
    todo_list = Blog.objects.all()
    return render(request, "add_items.html", {"blog": todo_list})
    
"""
def About(request):
    return render(request,"about.html")

def get_data_by_id(request,id):
    print("request",request)
    todo_list = Blog.objects
    
    context = {
        "items": todo_list,
    "html_title": "Views Items Page"
    }
    return render(request,"about.html",context)"""