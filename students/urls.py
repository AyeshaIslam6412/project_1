from django.urls import path
from.views import Student_list,add_student,update_student,delete_student

urlpatterns = [
    
    path("",Student_list,name="student-list"),
    path("add/",add_student,name="add_student"),
    path('update/<int:id>/',update_student,name='update-student'),
    path('delete/<int:id>/',delete_student,name='delete-student'),
    
]
