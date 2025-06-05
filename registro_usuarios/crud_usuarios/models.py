from django.db import models

class Usuario(models.Model):
    nombre = models.TextField(max_length=20)
    apellidos = models.TextField(max_length=20)
    numero_Identificacion= models.TextField(max_length=20)
    fecha_nacimiento = models.DateField()
    fecha_contratacion= models.DateTimeField(auto_now=True)
    numero_telefonico = models.TextField(max_length=15)
    direccion = models.TextField(max_length=20)

    class Meta:
        ordering = ['- fecha_nacimiento']


