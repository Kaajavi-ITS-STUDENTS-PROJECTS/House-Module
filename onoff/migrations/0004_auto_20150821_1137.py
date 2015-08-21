# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onoff', '0003_auto_20150810_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('status', models.BooleanField(default=False, verbose_name='Status general de la habitacion')),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
            },
        ),
        migrations.AlterField(
            model_name='luz',
            name='lugar',
            field=models.ForeignKey(to='onoff.Habitacion'),
        ),
        migrations.AlterField(
            model_name='puerta',
            name='lugar',
            field=models.ForeignKey(to='onoff.Habitacion'),
        ),
        migrations.DeleteModel(
            name='Cuarto',
        ),
    ]
