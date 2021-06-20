from django.db import models

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    description = models.TextField()
    demo_url = models.TextField(default="https://fourskilllevels.com")
    info_url = models.TextField(default="https://fourskilllevels.com")
    
    image = models.ImageField(default='project.png')
    added_date = models.DateTimeField(auto_now_add=True)
    
    
    
    
    def __str__(self):
        return self.name


class skill(models.Model):
    name = models.CharField(max_length=250)
    icon_url = models.TextField()
    description = models.TextField(blank=True)
    percentage = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name