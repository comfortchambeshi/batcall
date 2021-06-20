
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    
    path('', views.blog_home, name="blog_home"),
    path('<int:blog_id>', views.blog_detail, name="blog_id"),
   


]
