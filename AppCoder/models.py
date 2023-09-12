from django.db import models
from django.utils import timezone

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    fecha_creacion = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.nombre} - {self.camada}'
    


class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Estudiante(Persona):
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Profesor(Persona):
    profesion = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso, blank=True)

class Entregable(models.Model):

    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=256, null=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)