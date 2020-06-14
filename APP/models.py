from django.db import models
from django.utils import timezone

class Cliente (models.Model):
    nombre = models.CharField(max_length=30, default='DEFAULT VALUE')
    apellido=models.CharField(max_length=30,default='DEFAULT VALUE')
    correo=models.EmailField()
    telefono=models.CharField(max_length=11)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class TablaEmpleado:
        db_table='Cliente'


class Empleado (models.Model):
    nombre = models.CharField(max_length=30, default='DEFAULT VALUE')
    apellido=models.CharField(max_length=30,default='DEFAULT VALUE')
    correo=models.EmailField()
    telefono=models.CharField(max_length=11)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class TablaEmpleado:
        db_table='Empleado'

class Postres(models.Model):
    nombre= models.CharField(max_length=30, default='DEFAULT VALUE')
    precio=models.CharField(max_length=20,default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class TablaPostre:
        db_table='postre'

class Menu(models.Model):
    nombre = models.CharField(max_length=30, default='DEFAULT VALUE')
    precio = models.CharField(max_length=20, default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class TablaMenu:
        db_table='menu'

class Bebida(models.Model):
    nombre = models.CharField(max_length=30, default='DEFAULT VALUE')
    precio = models.CharField(max_length=20, default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class TablaBebida:
        db_table='bebida'


