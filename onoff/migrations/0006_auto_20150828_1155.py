# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onoff', '0005_alarma_sanitario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarma',
            name='status',
        ),
        migrations.RemoveField(
            model_name='luz',
            name='status',
        ),
        migrations.RemoveField(
            model_name='puerta',
            name='status',
        ),
        migrations.AddField(
            model_name='alarma',
            name='pin',
            field=models.IntegerField(default=1, verbose_name='Pin'),
        ),
        migrations.AddField(
            model_name='luz',
            name='pin',
            field=models.IntegerField(default=1, verbose_name='Pin'),
        ),
        migrations.AddField(
            model_name='puerta',
            name='pin',
            field=models.IntegerField(default=1, verbose_name='Pin'),
        ),
    ]
