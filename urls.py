# weatherapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_weather, name='weather'),
]
