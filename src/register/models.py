from django.db import models

# Create your models here.
class Estudiante(models.Model):
    num_manilla = models.IntegerField(primary_key=True)
    codigo = models.IntegerField(unique=True)
    cedula = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=50)
    programa = models.CharField(max_length=50)
    tel_familiar = models.CharField(max_length=10)
    familiar = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    photo = models.ImageField(null=True, blank=True)
    observacion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Registro(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    ingreso = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    salida = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    observacion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.estudiante.nombre
