"""
URL configuration for eduviaje project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios import  views as userViews
from conductores import views as driverViews
from viajes import views as viajesViews

import usuarios.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userViews.index, name='index'),
    path('Perfil/<int:id>/', userViews.retrieve , name='retrieve'),
    path('Perfil/<int:id>/Edit', userViews.edit, name='edit'),
    path('login/User',userViews.login, name='loginU'),
    path('login/Driver',driverViews.login, name='loginD'),
    path('registro', userViews.seleccion, name="selection"),
    path('conducto',driverViews.create,name='create'),
    path('usuario',userViews.create,name='create2'),
    path('viajar',driverViews.recibirViaje ,name='viajar'),
    path('crear',userViews.crearViaje, name="crearViaje"),
]
