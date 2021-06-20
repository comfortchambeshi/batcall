from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pricing'
urlpatterns = [
    
    path('', views.pricing, name="pricing_home"),
    
   


]
