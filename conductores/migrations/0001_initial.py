# Generated by Django 5.0.4 on 2024-08-09 03:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo_electronico', models.EmailField(max_length=254, unique=True)),
                ('contrasena', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('historial_viajes', models.TextField()),
                ('calificacion', models.FloatField(default=0.0)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculo')),
            ],
        ),
    ]