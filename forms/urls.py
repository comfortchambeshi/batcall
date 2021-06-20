from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'forms'

urlpatterns = [
    
    path('', views.main_page, name="main_forms"),
    path('hire/', views.hire_page, name="hire_form"),
    path('contact/', views.contact_page, name="contact_form"),
    path('success/', views.success_page, name="success_page"),
    
    
    


]