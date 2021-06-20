from django.urls import path, include
from . import views

app_name = "importants"
urlpatterns = [
    path('', views.importants_home, name="importants_home"),
    path('read/<str:pk>/', views.read_important, name="read_important"),
]


