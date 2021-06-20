from django.shortcuts import render,redirect
from django.http import HttpResponse
from pricing.models import pricing
from django import forms
from .forms import contactForm
from .forms import HireForm


# Create your views here.


def main_page(request):
    current_url = request.path
    return render(request, 'forms/forms.html', {'current_url':current_url})

def hire_page(request):
    hireform = HireForm()
    if request.method == "POST":
        hireform = HireForm(request.POST)
        if hireform.is_valid():
            hireform.save()
            return redirect('/forms/success')
        
    services = pricing.objects.all()
    context = {'services':services, 'hireform':hireform}
    return render(request,'forms/forms.html', context)

def contact_page(request):
    form = contactForm()    
    if request.method == "POST":
            form = contactForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/forms/success')
    context = {'form':contactForm}               
    return render(request,'forms/forms.html', context)
    

def success_page(request):
    return render(request, 'forms/success.html')
    
    
    
    
    
    