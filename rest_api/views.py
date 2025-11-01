from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views APIView

@api_view(["GET"])
def get_data(request):


    student = Student.objects.all()
    serializer = StudentSerializer(student,many=True)
    return Response(serializer.data)
