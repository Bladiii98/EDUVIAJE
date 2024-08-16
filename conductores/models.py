from django.db import models
from vehiculos.models import Vehiculo  # Importar el modelo relacionado


class Conductor(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    vehicle = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True)
    history = models.TextField(default="")
    score = models.FloatField(default=0.0)

    # Métodos: registrarse(), aceptarViaje(), etc.


