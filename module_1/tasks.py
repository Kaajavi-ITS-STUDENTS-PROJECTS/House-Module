from __future__ import absolute_import

from celery import shared_task

#@shared_task para que no dependa de un proyecto completo para andar sino que la app puede hacer las funciones en cualquier lado que este celery
@shared_task
def add(x, y):
    return x + y
