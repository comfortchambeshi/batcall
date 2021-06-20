from django.db import models

# Create your models here.

class pricing(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField('price',max_length=11)
    currency = models.CharField(max_length=250)
    currency_symbol = models.CharField(default='ZMW',max_length=250)
    description = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
