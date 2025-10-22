from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length= 20)
    description = models.CharField(max_length= 1000)
    creat_at = models.DateTimeField(auto_now_add=True ,blank=True,null=True)


    
    def __str__(self):
        return f"{self.title}"
    
    
    