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

def recibirViaje(request):

    if request.method == 'POST':
        origin = request.POST['origin']
        destiny = request.POST['destiny']
        userId = request.POST['userId']
        costo = request.POST['costo']
        viaje = Viaje(origin=origin,destiny=destiny,user=Usuario.objects.get(pk=userId),status=False,cost=costo)
        viaje.save()
        viajes = Viaje.objects.all()
        conductor = Conductor.objects.all()
        return render(request, 'RecibirViaje.html', {"viajes": viajes, "conductor": conductor})

    viajes = Viaje.objects.all()
    conductor = Conductor.objects.all()
    return render(request, 'RecibirViaje.html' ,{"viajes": viajes,"conductor":conductor})