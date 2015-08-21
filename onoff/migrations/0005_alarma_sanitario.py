# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onoff', '0004_auto_20150821_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Alarma',
                'verbose_name_plural': 'Alarmas',
            },
        ),
        migrations.CreateModel(
            name='Sanitario',
            fields=[
                ('habitacion_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='onoff.Habitacion')),
                ('ocupado', models.BooleanField(default=False, verbose_name='Ocupado')),
            ],
            options={
                'verbose_name': 'Sanitario',
                'verbose_name_plural': 'Sanitarios',
            },
            bases=('onoff.habitacion',),
        ),
    ]
