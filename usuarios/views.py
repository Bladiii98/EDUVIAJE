from django.shortcuts import render, redirect
from .models import Usuario


# Create your views here.
def index(request):
    return render(request, 'index.html')


def retrieve(request, id):
    perfil = Usuario.objects.get(pk=id)
    return render(request, 'Perfil.html', {"perfil": perfil})


def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        phone = request.POST['phone']
        accountNumber = request.POST['accountNumber']
        password = request.POST['password']

        perfil = Usuario(name=name, mail=mail, phone=phone, accountNumber=accountNumber, password=password)
        perfil.save()

        return redirect('index')

    return render(request, 'Usuario.html')


def seleccion(request):
    return render(request, "seleccion.html")


def edit(request, id):
    perfil = Usuario.objects.get(pk=id)

    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        phone = request.POST['phone']

        perfil.name = name
        perfil.mail = mail
        perfil.phone = phone
        perfil.save()
        return redirect('index')

    return render(request, 'Edit.html', {"perfil": perfil})


def login(request):
    if request.method == 'POST':
        usuario = Usuario.objects.get(name="asdasd")
        if usuario.password == request.POST['password']:
            return render(request, "index.html", {"usuario": usuario})
        else:
            pass

    return render(request, 'login.html')
