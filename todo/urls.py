from django.urls import path
from .views import home,show_items,create,get_all, see_all

urlpatterns = [
   
    path("home/",home,name="home"),
    path("items/",show_items,name="items"),
    path("add-items/", create, name="add-items"),
    path("get-all/", get_all, name="get-all"),
    path("see_all/", see_all, name="see_all"),
]
