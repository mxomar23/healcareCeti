from django.db import models
from Alergia.models import Alergia
# Create your models here.


class Paciente(models.Model):
    sexo_tipo = (
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=6, choices=sexo_tipo)
    fecha_nacimiento = models.DateField()
    sala_piso = models.CharField(max_length=100)
    receta = models.CharField(max_length=100)
    alergias = models.ManyToManyField(Alergia)
    expediente = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagen_perfil', blank=True, null=True)

    def __str__(self):
        return 'Paciente: %s %s, en: %s' % (self.nombre, self.apellido, self.sala_piso)
