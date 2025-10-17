from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length= 100)
    author = models.CharField(max_length= 50)
    description = models.TextField(blank=False)
    gfdhgjhgffds
    
    def __str__(self):
        return f"{self.title}"
    
    
    