from django.contrib import admin
from django.urls import path
from alumnos import views


urlpatterns = [
    path('', views.inicio ,name="Inicio"),
]