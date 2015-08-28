# -*- coding: utf-8 -*-

from django.db import models

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
    
    nombre = models.CharField(u"Nombre",max_length=200)
    status = models.BooleanField(u'Status', default=False)
    pin = models.IntegerField(u'Pin', default=1)
    lugar = models.ForeignKey(Habitacion)
    
    def __str__(self):
        return self.nombre

class Puerta(models.Model):
    class Meta:
        verbose_name = "Puerta"
        verbose_name_plural = "Puertas	"
    
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

