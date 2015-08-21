# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onoff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luz',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='luz',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
    ]
