from django.db import models
from usuarios.models import Usuario
from conductores.models import Conductor

class Viaje(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    dirver = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    origin = models.CharField(max_length=255)
    destiny = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    cost = models.FloatField()

    # Métodos: iniciarViaje(), completarViaje(), etc.
