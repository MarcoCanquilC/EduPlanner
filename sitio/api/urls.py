# api/urls.py
from django.urls import path
from . import views

#Direcciones de la API.
urlpatterns = [
    path("calendario/", views.calendario_academico, name="calendario_academico")
]