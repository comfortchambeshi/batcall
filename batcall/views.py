from django.http import HttpResponse
from django.shortcuts import render
from pricing.models import pricing
from portifolio.models import *


def homepage(request):
    pricings = pricing.objects.all()
    skills =  skill.objects.all()
    projects = project.objects.all()
    context  = {'pricings':pricings, 'projects':projects, 'skills':skills}
    
    return render(request, 'homepage.html', context)