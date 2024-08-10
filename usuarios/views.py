from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.
def index(request):
    return render(request, 'index.html')

def retrieve(request, id):
    perfil = Usuario.objects.get(pk = id)
    return render(request,'Perfil.html', {"perfil":perfil})
def create(request):
    nombre = request.POST['nombre']
    correo_electronico = request.POST['correo_electronico']
    telefono = request.POST['telefono']


    perfil = Usuario(nombre=nombre,correo_electronico=correo_electronico,telefono=telefono)
    perfil.save()

    return redirect('index')


