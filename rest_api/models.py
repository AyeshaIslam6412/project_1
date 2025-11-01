from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=False,null=False)
    course = models.CharField(blank=False)