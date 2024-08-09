from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    metodo_pago = models.CharField(max_length=50)
    calificacion_usuario = models.FloatField(default=0.0)
    historial_viajes = models.TextField()

    # Métodos: registrarse(), iniciarSesion(), etc.
