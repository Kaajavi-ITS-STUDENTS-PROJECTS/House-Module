# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onoff', '0009_delete_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='luz',
            options={'verbose_name': 'Luz', 'verbose_name_plural': 'Luces', 'permissions': (('prender_luz', 'Puede prender luz'),)},
        ),
    ]
