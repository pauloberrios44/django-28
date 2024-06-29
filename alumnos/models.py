from django.db import models

# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(db_column="idGenero", primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

class Curso(models.Model):
    id_curso = models.AutoField(db_column="idCurso", primary_key=True)
    nombre_curso = models.CharField(max_length=100, blank=False, null=False)
    suspendido = models.IntegerField()

class Alumno(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()

class Navbar(models.Model):
    id_navbar = models.AutoField(db_column="idNavbar", primary_key=True)
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=100)