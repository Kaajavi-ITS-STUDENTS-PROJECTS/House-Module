# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onoff', '0006_auto_20150828_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarma',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='luz',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='puerta',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
    ]
