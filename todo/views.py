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
        result += f'<h3>{blog.description}</h3>'
    return HttpResponse(result)


def index(request):
    todo_list = Blog.objects.all()
    print(todo_list)
    
    for q in todo_list:
        print("title",q.title)
        print("author",q.author)
        print("description",q.description)
    output = ",".join([q.author for q in todo_list])
    return HttpResponse(output)

def about(request):
    return HttpResponse("this is about page")


def get_all(request):
    return HttpResponse("")