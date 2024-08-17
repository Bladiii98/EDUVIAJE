# Generated by Django 5.0.4 on 2024-08-09 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo_electronico', models.EmailField(max_length=254, unique=True)),
                ('contrasena', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('metodo_pago', models.CharField(max_length=50)),
                ('calificacion_usuario', models.FloatField(default=0.0)),
                ('historial_viajes', models.TextField()),
            ],
        ),
    ]
