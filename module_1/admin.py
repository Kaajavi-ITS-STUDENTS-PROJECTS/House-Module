# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Luz, Habitacion, Puerta, Alarma, Usuario, Regla, Log, Mapa, Objeto
# Register your models here.
admin.site.register(Luz)
admin.site.register(Habitacion)
admin.site.register(Puerta)
admin.site.register(Alarma)
admin.site.register(Usuario)
admin.site.register(Regla)
admin.site.register(Log)
admin.site.register(Mapa)
admin.site.register(Objeto)
