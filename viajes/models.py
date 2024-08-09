from django.db import models
from usuarios.models import Usuario
from conductores.models import Conductor

class Viaje(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    origen = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    estado = models.CharField(max_length=50)
    costo = models.FloatField()

    # Métodos: iniciarViaje(), completarViaje(), etc.
