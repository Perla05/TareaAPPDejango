"""AgendaContactos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Agenda.views import ListadoContactos,DetalleContactos, CrearContactos,ActualizarContacto,EliminarContacto

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),

    # La ruta 'leer' en donde listamos todos los registros de la Base de Datos
    path ('index/', ListadoContactos.as_view(template_name ="template/contactos/index.html"), name= 'leer'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro
    path('contactos/detalle/<int:pk>', DetalleContactos.as_view(template_name= "/template/contactos/detalles.html"), name='detalles'),

    #La ruta crear en donde mostraremos un formulario para crear un nuevo contacto
    path('contactos/crear', CrearContactos.as_view(template_name="contactos/crear.html"), name='crear'),

    # La ruta actualizar en donde mostraremos un formulario para actualizar un nuevo contacto
    path('contactos/editar/<int:pk>', ActualizarContacto.as_view(template_name="contactos/actualizar.html"), name='actualizar'),

    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos
    path('contactos/eliminar/<int:pk>', EliminarContacto.as_view(), name='eliminar'),

]
