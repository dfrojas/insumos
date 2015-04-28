# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hato', '0002_auto_20150427_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametroproductivodobleproposito',
            name='dias_abiertos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parametroproductivodobleproposito',
            name='duracion_lactancia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parametroproductivodobleproposito',
            name='litro_vaca_dia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parametroproductivodobleproposito',
            name='peso_cria_nacimiento',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
