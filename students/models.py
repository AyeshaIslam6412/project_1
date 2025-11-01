from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length= 20)
    Age = models.IntegerField(blank=False)
    Course = models.CharField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return self.Name
    
    