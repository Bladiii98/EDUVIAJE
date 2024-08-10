from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    accountNumber = models.CharField(max_length=15 , unique=True)
    paymentMethod = models.CharField(max_length=50)
    score = models.FloatField(default=0.0) #Calificacion
    history = models.TextField(default="")


    # Métodos: registrarse(), iniciarSesion(), etc.
