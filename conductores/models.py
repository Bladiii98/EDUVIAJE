from django.db import models
from vehiculos.models import Vehiculo  # Importar el modelo relacionado

class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    # vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    # historial_viajes = models.TextField()
    # calificacion = models.FloatField(default=0.0)

    # Métodos: registrarse(), aceptarViaje(), etc.
