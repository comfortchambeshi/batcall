from django.shortcuts import render
from .models import pricing

# Create your views here.

def pricing(request):
    pricing = pricing.objects.all()
    return render(request, 'homepage.html', {'pricing':pricing})
    

    
    
