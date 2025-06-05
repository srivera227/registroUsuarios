from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    numero_Identificacion= models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    #fecha_contratacion= models.DateTimeField(auto_now=True , editable=False)
    numero_telefonico = models.CharField(max_length=15)
    direccion = models.CharField(max_length=20)

    class Meta:
        ordering = ['-fecha_nacimiento']


