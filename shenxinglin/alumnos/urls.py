from django.contrib import admin
from django.urls import path
from alumnos import views


urlpatterns = [
    path('', views.inicio ,name="Inicio"),
    path('noticias', views.noticias, name="Noticias"),
    path('alumnos', views.alumnos, name="Alumnos"),
    path('staff', views.staff, name="Staff"),
    path('escuela', views.escuela, name="Escuela"),
]