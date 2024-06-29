from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    Alumnos = Alumno.objects.all()  # SELECT * FROM ALUMNOS;
    Cursos = Curso.objects.all() # SELECT * FROM alumnos_cursos
    Navbars = Navbar.objects.all() # SELECT * FROM alumnos_navbar
    context = {
        "Alumnos": Alumnos,
        "Cursos": Cursos,
        "Navbars": Navbars
    }
    return render (request, 'alumnos/index.html', context)

def misAsignaturas(request):
    Alumnos = Alumno.objects.all()  # SELECT * FROM ALUMNOS;
    Cursos = Curso.objects.all() # SELECT * FROM alumnos_cursos
    Navbars = Navbar.objects.all() # SELECT * FROM alumnos_navbar
    context = {
        "Alumnos": Alumnos,
        "Cursos": Cursos,
        "Navbars": Navbars
    }
    return render (request, 'alumnos/misasignaturas.html', context)

def Contacto(request):
    Navbars = Navbar.objects.all() # SELECT * FROM alumnos_navbar
    context = {
        "Navbars": Navbars
    }
    return render (request, 'alumnos/contacto.html', context)