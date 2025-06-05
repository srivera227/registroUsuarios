from django import forms
from .models import Usuario

class formularioRegistro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','apellidos','numero_Identificacion','fecha_nacimiento','numero_telefonico','direccion']
