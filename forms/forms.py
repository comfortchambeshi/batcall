from django import forms

from .models import *

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields =  '__all__'
        
     
        widgets = {
            'full_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Your name'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'Your email address', 'type': 'email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder' : 'Your message to me....'}),
        }
        
        
class HireForm(forms.ModelForm):
    class Meta:
        model = hire
        fields = '__all__'
        
        widgets = {
            'customer_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name or organization'}),
            'email' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Email'}),
            'budget': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Budget'}),
            'service': forms.Select(attrs={'class':'form-control','label': 'Choose a service'}),
            'project_description': forms.Textarea(attrs={'class':'form-control','placeholder': 'Project description'})
            
            
            
        }
        
        