from django.urls import path
from .views import home,show_items, index,about,get_all

urlpatterns = [
    path("index/",index,name="index"),
    path("about/",about,name="about"),
    path("home/",home,name="home"),
    path("items/",show_items,name="items"),
    path("get_all/",get_all,name="get_all"),
]
