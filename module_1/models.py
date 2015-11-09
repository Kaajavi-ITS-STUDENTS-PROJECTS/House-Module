# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Habitacion(models.Model):
    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    nombre = models.CharField(u'Nombre', max_length=200)
    status = models.BooleanField (u'Status general de la habitacion', default=False)

    def __str__(self):
        return self.nombre


            
class Luz(models.Model):
    class Meta:
        verbose_name = "Luz"
        verbose_name_plural = "Luces"
        permissions = (
            ("prender_luz", "Puede prender luz"),
        )
    
    nombre = models.CharField(u"Nombre",max_length=200)
    status = models.BooleanField(u'Status', default=False)
    pin = models.IntegerField(u'Pin', default=1)
    lugar = models.ForeignKey(Habitacion)
    
    def __str__(self):
        return self.nombre

class Puerta(models.Model):
    class Meta:
        verbose_name = "Puerta"
        verbose_name_plural = "Puertas  "
    
    nombre = models.CharField(u"Nombre",max_length=200)
    status = models.BooleanField(u'Status', default=False)
    pin = models.IntegerField(u'Pin', default=1)
    auto_close = models.BooleanField(u'Auto Close', default=True)
    lugar = models.ForeignKey(Habitacion)
    
    def __str__(self):
        return self.nombre

class Sanitario(Habitacion):
    class Meta:
        verbose_name = "Sanitario"
        verbose_name_plural = "Sanitarios"
    
    ocupado = models.BooleanField(u'Ocupado', default=False)
    
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
    
    
    def __str_(self):
        return self.relacion.nombre


class Log(models.Model):
    fecha = models.DateField(u"Fecha")
    logs = JSONField()

    