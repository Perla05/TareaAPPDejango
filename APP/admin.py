from django.contrib import admin
from Agenda.models import Cliente
from Agenda.models import Empleado
from Agenda.models import Postres
from Agenda.models import Bebida
from Agenda.models import Menu

admin.site.register(Empleado),
admin.site.register(Cliente),
admin.site.register(Postres),
admin.site.register(Bebida),
admin.site.register(Menu)