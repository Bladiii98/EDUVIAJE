from django.shortcuts import render, redirect
from .models import Conductor

# Create your views here.
def create(request):

    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo_electronico = request.POST['correo_electronico']
        contrasena = request.POST['contrasena']


        perfil = Conductor(nombre=nombre,correo_electronico=correo_electronico,contrasena=contrasena)
        perfil.save()
        return redirect('index')

    return render(request, 'Conductor.html')