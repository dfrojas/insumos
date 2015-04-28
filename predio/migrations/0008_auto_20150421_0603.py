# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0007_auto_20150421_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viviendapredio',
            name='bateria_sanitaria',
            field=models.ForeignKey(to='opciones.Booleanos', blank=True, related_name='booleanos+', null=True),
        ),
        migrations.AlterField(
            model_name='viviendapredio',
            name='cubierta',
            field=models.ForeignKey(to='opciones.Cubierta', blank=True, related_name='cubierta+', null=True),
        ),
        migrations.AlterField(
            model_name='viviendapredio',
            name='energia_alternativa',
            field=models.ForeignKey(to='opciones.Booleanos', blank=True, related_name='booleanos+', null=True),
        ),
        migrations.AlterField(
            model_name='viviendapredio',
            name='energia_electrica',
            field=models.ForeignKey(to='opciones.Booleanos', blank=True, related_name='booleanos+', null=True),
        ),
        migrations.AlterField(
            model_name='viviendapredio',
            name='energia_preparacion_alimentos',
            field=models.ForeignKey(to='opciones.FuenteEnergiaPreparacionAlimentos', blank=True, related_name='fuente energia+', null=True),
        ),
        migrations.AlterField(
            model_name='viviendapredio',
            name='estado_saneamiento',
            field=models.ForeignKey(to='opciones.BMR', blank=True, related_name='bueno malo regular+', null=True),
        ),
        migrations.AlterField(
            model_name='viviendapredio',
            name='fuente_energia',
            field=models.ForeignKey(to='opciones.FuenteEnergia', blank=True, related_name='fuente energia+', null=True),
        ),
        migrations.AlterField(
            model_name='viviendapredio',
            name='posee_vivienda',
            field=models.ForeignKey(to='opciones.Booleanos', blank=True, related_name='booleanos+', null=True),
        ),
        migrations.AlterField(
            model_name='viviendapredio',
            name='tipo_construccion',
            field=models.ForeignKey(to='opciones.TipoConstruccion', blank=True, related_name='tipo construccion+', null=True),
        ),
    ]
