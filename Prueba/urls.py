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
from Agenda.views import  HomeView
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),

    path('formulario1/', HomeView.formulario1, name='formulario1'),

    path('formulario2/', HomeView.formulario2, name='formulario2'),

    path('formulario3/', HomeView.formulario3, name='formulario3'),

    path('formulario4/', HomeView.formulario4, name='formulario4'),

    path('formulario5/', HomeView.formulario5, name='formulario5'),


]