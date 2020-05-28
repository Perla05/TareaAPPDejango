from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contactos
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares
from django.urls import  reverse

#Habilitamos el uso de mensajes en Django
from django.contrib import messages
from django.contrib.messages.views import  SuccessMessageMixin

#Habilitamos los mensajes para class-based views

#Habilitamos los formularios en Django

from django import forms

class ListadoContactos(ListView):
    model = Contactos

class DetalleContactos(DetailView):
    model = Contactos

class CrearContactos(SuccessMessageMixin,CreateView):
    model = Contactos
    form = Contactos
    fields = "__all__"
    success_message =  'Contacto creado Correctamente'

    #Redireccionamos a la pagina principal luego de crear un registro
    def get_success_url(self):
        return reverse('leer') #Redireccionamos a la vista principal

class ActualizarContacto(SuccessMessageMixin, UpdateView):
    model = Contactos
    form = Contactos
    fields = '__all__'
    success_message =  'Contacto Actualizado Correctamente'

    #Redireccionamos a la clase principal
    def get_success_url(self):
        return reverse('leer')

class EliminarContacto (SuccessMessageMixin, DeleteView):
    model = Contactos
    form = Contactos
    fields = '__all__'

    #Redireccionamos a la pagina principal
    def get_success_url(self):
        success_message ='Contacto Eliminado Correctamente'
        messages.success(self.request, (success_message))
        return reverse('leer')


