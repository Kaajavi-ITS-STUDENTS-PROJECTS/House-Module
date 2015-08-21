# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Luz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Titulo')),
                ('status', models.BooleanField(default=True, verbose_name='Publicado?')),
            ],
            options={
                'verbose_name': 'Luz',
                'verbose_name_plural': 'Luces',
            },
        ),
    ]
