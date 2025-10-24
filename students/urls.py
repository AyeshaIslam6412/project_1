from django.urls import path
from .views import Student_list,update_student,create,delete_student

urlpatterns = [
    
    path("",Student_list,name="student-list"),
    path("add/",create,name='add-student'),
    path('update/<int:id>/',update_student,name='update-student'),
    path('delete/<int:id>/',delete_student,name='delete-student'),
    
]
