from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.
def index(request):
    return render(request, 'index.html')

def retrieve(request, id):
    perfil = Usuario.objects.get(pk = id)
    return render(request,'Perfil.html', {"perfil":perfil})


