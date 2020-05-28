from django.db import models

# Create your models here.

class Contactos(models.Model):
    nombre=models.CharField(max_length=30, default='DEFAULT VALUE')
    apellido=models.CharField(max_length=30,default='DEFAULT VALUE')
    correo=models.EmailField()
    telefono=models.CharField(max_length=11)
    fotografia=models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Meta:
    db_table='contactos'

