from django.db import models

class Vehiculo(models.Model):
    tipo = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10, unique=True)
    capacidad = models.IntegerField()
    marca = models.CharField(max_length=50)

    # Métodos: actualizarEstado()
