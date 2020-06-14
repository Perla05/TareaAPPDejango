from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from .models import Contactos
from .models import Cliente
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares
from django.urls import  reverse

#Habilitamos el uso de mensajes en Django
from django.contrib import messages

#Habilitamos los mensajes para class-based views

from django.contrib.messages.views import  SuccessMessageMixin
#Habilitamos los formularios en Django
from django import forms

class HomeView():
    def home (self):
        plantilla = get_template('base.html')
        return HttpResponse(plantilla.render())

    def formulario1 (self):
        plantilla = get_template('formulario1.html')
        return HttpResponse(plantilla.render())

    def formulario2 (self):
        plantilla = get_template('formulario2.html')
        return HttpResponse(plantilla.render())

    def formulario3 (self):
        plantilla = get_template('formulario3.html')
        return HttpResponse(plantilla.render())

    def formulario4 (self):
        plantilla = get_template('formulario4.html')
        return HttpResponse(plantilla.render())

    def formulario5 (self):
        plantilla = get_template('formulario5.html')
        return HttpResponse(plantilla.render())



