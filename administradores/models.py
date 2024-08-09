from django.db import models

class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)

    # Métodos: gestionarUsuarios(), resolverDisputas(), etc.
