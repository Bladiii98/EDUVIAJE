from django.shortcuts import render, redirect
from .models import Conductor

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