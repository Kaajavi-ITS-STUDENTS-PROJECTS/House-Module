# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
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
    def __str__(self):
        return self.user.username
    
    
    
    
    
class Regla(models.Model):
    lunes = 'lun'
    martes = 'mar'
    miercoles = 'mie'
    jueves = 'jue'
    viernes = 'vie'
    sabado = 'sab'
    domingo = 'dom'
    dias_semana = (
        (lunes, 'Lunes'),
        (martes, 'Martes'),
        (miercoles, 'Miercoles'),
        (jueves, 'Jueves'),
        (viernes, 'Viernes'),
        (sabado, 'Sabado'),
        (domingo, 'Domingo'),
    )
    dias_de_semana = models.CharField(max_length=3,
                                      choices=dias_semana,)
    
    from_hour = models.TimeField(u'Start', blank=True)
    to_hour = models.TimeField(u'End', blank=True)
    relacion = models.ForeignKey(Luz)
    pin = models.IntegerField(u'Pin', default=1)
    status = models.BooleanField(u'Status', default=False)
    
    
    def __str_(self):
        return self.relacion.nombre
