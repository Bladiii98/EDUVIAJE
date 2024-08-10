from django.db import models

class Vehiculo(models.Model):
    type = models.CharField(max_length=50)
    registry = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField()
    brand = models.CharField(max_length=50)

    # Métodos: actualizarEstado()
