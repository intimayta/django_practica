from django.urls import path
from . import views

urlpatterns = [
    path("", views.indice, name="inicio"),
    path("acerca/", views.acerca, name="acerca"),
    path("temario/", views.temario, name="temario"),

    path("pato", views.pato, name="pato"),
    path("vaca", views.vaca, name="vacas"),
    path("perro", views.perro, name="Perro")
]