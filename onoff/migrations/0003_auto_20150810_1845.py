# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onoff', '0002_auto_20150810_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuarto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('status', models.BooleanField(default=False, verbose_name='Status general del cuarto')),
            ],
            options={
                'verbose_name': 'Cuarto',
                'verbose_name_plural': 'Cuartos',
            },
        ),
        migrations.CreateModel(
            name='Puerta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('lugar', models.ForeignKey(to='onoff.Cuarto')),
            ],
            options={
                'verbose_name': 'Puerta',
                'verbose_name_plural': 'Puertas\t',
            },
        ),
        migrations.AlterField(
            model_name='luz',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='luz',
            name='lugar',
            field=models.ForeignKey(default=2, to='onoff.Cuarto'),
            preserve_default=False,
        ),
    ]
