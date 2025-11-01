from django.urls import path
from .views import  register,login_view,sign_out

urlpatterns = [
    
    path("registration/",register,name="registration"),
    path("login/",login_view,name="Log-in"),
    path("logout/",sign_out,name="sign-out"),
    
    
]
