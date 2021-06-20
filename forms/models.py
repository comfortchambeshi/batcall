from django.db import models
from pricing.models import pricing

# Create your models here.

class hire(models.Model):
    customer_name = models.CharField(max_length= 250)
    email = models.CharField(max_length= 250)
    budget = models.CharField(max_length= 250)
    service = models.ForeignKey(pricing,on_delete=models.CASCADE)
    project_description = models.TextField()
    submitted_date= models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self):
        return self.customer_name
        
        
class contact(models.Model):
    full_name = models.CharField(max_length= 250)
    email = models.CharField(max_length= 250)
    message = models.TextField()
    submitted_date= models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self):
        return self.full_name        
    
    
    
    
    
