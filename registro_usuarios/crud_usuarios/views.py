from django.shortcuts import render,redirect
from .models import Usuario
from.forms import formularioRegistro


# Create your views here.

def mostrarUsuarios(request):
    usuario = Usuario.objects.all()
    usuarioEncontrado = None
    form = formularioRegistro()

    if request.method == 'POST':
        if 'registrar' in request.POST:
            form = formularioRegistro(request.POST)
            if form.is_valid():
                form.save()
                print("Usuario registrado correctamente.")
                return redirect('registro:lista_registro')  
            else:
                print("Errores del formulario:", form.errors)

        elif 'editar' in request.POST:
            id_usuario = request.POST.get('campoId', '').strip()
            print(f"ID recibido: '{id_usuario}'")
            if id_usuario:
                try:
                    usuarioEncontrado = Usuario.objects.get(numero_Identificacion=id_usuario)
                except Usuario.DoesNotExist:
                    print("Usuario no encontrado.")
                    usuarioEncontrado = None

    return render(request, 'vistaUsuarios.html', {
        'form': form,
        'usuario': usuario,
        'usuario_encontrado': usuarioEncontrado  })





        












