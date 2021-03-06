# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
class Habitacion(models.Model):
    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    nombre = models.CharField(u'Nombre', max_length=200)
    status = models.BooleanField (u'Status general de la habitacion', default=False)

    def __str__(self):
        return self.nombre


class Objeto(models.Model):
    nombre = models.CharField(u"Nombre",max_length=200)
    status = models.BooleanField(u'Status', default=False)
    lugar = models.ForeignKey(Habitacion)
    dibujo_y = models.IntegerField(u'Posicion en mapa, y', default=0)
    dibujo_x = models.IntegerField(u'Posicion en mapa, x', default=0)
            
class Luz(Objeto):
    class Meta:
        verbose_name = "Luz"
        verbose_name_plural = "Luces"
        permissions = (
            ("prender_luz", "Puede prender luz"),
        )
    pin = models.IntegerField(u'Pin', default=1)
    def __str__(self):
        return self.nombre

class Puerta(Objeto):
    class Meta:
        verbose_name = "Puerta"
        verbose_name_plural = "Puertas  "
    auto_close = models.BooleanField(u'Auto Close', default=True)
    pin = models.IntegerField(u'Pin', default=1)
    def __str__(self):
        return self.nombre

class Alarma(models.Model):
    class Meta:
        verbose_name = "Alarma"
        verbose_name_plural = "Alarmas"
    
    nombre = models.CharField(u"Nombre",max_length=200)
    status = models.BooleanField(u'Status', default=False)
    pin = models.IntegerField(u'Pin', default=1)
    
    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    user = models.OneToOneField(User, related_name="permisos")
    permisos_luces = models.ManyToManyField(Luz,blank=True)
    permisos_puertas = models.ManyToManyField(Puerta,blank=True)
    permisos_habitaciones = models.ManyToManyField(Habitacion,blank=True)
    img = models.FileField(u'Profile Image',upload_to = 'img_perfil', default='null')
    def __str__(self):
        return self.user.username
    
class Regla(models.Model):
    lun = models.BooleanField(u'Lunes', default=False)
    mar = models.BooleanField(u'Martes', default=False)
    mie = models.BooleanField(u'Miercoles', default=False)
    jue = models.BooleanField(u'Jueves', default=False)
    vie = models.BooleanField(u'Viernes', default=False)
    sab = models.BooleanField(u'Sabado', default=False)
    dom = models.BooleanField(u'Domingo', default=False)
    
    from_hour = models.TimeField(u'Start')
    to_hour = models.TimeField(u'End')
    relacion = models.ForeignKey(Luz)
    pin = models.IntegerField(u'Pin', default=1)
    status = models.BooleanField(u'Status', default=False)
    
    
    def __str__(self):
        return self.relacion.nombre

    
    
class Mapa(models.Model):
    img = models.FileField(u'Mapa',upload_to = 'img_mapas', default='null')
    
    
    

class Log(models.Model):
    class Meta:
        verbose_name = "Log de Luz"
        verbose_name_plural = "Logs de Luces"
    fecha = models.DateField(u"Fecha", default=timezone.now)
    hora = models.TimeField(u'Hora',auto_now=True)
    output = models.ForeignKey(Objeto)
    status = models.BooleanField(u'Status', default=False)
    def __str__(self):
        if self.status==True:
            return self.output.nombre + "set on On"
        else:
            return self.output.nombre + "set on Off"


