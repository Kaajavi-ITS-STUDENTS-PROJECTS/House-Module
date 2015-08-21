# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Luz, Habitacion, Puerta, Sanitario, Alarma
# Register your models here.
admin.site.register(Luz)
admin.site.register(Habitacion)
admin.site.register(Puerta)
admin.site.register(Alarma)
admin.site.register(Sanitario)
