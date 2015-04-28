# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0007_actividadecoturismo_atractivoecoturismo'),
        ('predio', '0009_auto_20150422_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viviendapredio',
            name='energia_preparacion_alimentos',
        ),
        migrations.AddField(
            model_name='viviendapredio',
            name='energia_preparacion_alimentos',
            field=models.ManyToManyField(blank=True, to='opciones.FuenteEnergiaPreparacionAlimentos', null=True, related_name='fuente energia+'),
        ),
    ]
