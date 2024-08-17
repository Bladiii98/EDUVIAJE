from django.shortcuts import render, redirect
from .models import Conductor
from viajes.models import Viaje
from usuarios.models import Usuario

# Create your views here.
def create(request):

    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        password = request.POST['password']
        phone = request.POST['phone']


        perfil = Conductor(name=name,mail=mail,password=password,phone=phone)
        perfil.save()
        return redirect('index')

    return render(request, 'Conductor.html')

def login(request):
    if request.method == 'POST':
        conductor = Conductor.objects.get(name='name')
        if conductor.password == request.POST['password']:
            return redirect("index",{"conductor":conductor})
        else:
            pass

    return render(request, 'login.html')

def recibirViaje(request,id):
    viajes = Viaje.objects.all()
    conductor = Conductor.objects.get(pk=id)
    return render(request, 'RecibirViaje.html' ,{"viajes": viajes,"conductor":conductor})

def elegirViaje(request,iddriver,idviaje):
    if request.method == 'POST':
        conductor = Conductor.objects.get(pk=iddriver)
        viaje = Viaje.objects.get(pk=idviaje)
        viaje.driver = conductor
        viaje.save()
        return redirect('index')
