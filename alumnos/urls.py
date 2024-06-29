from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('mis-asignaturas', views.misAsignaturas, name="mis-asignaturas"),
    path('contacto', views.Contacto, name="contacto"),
]

