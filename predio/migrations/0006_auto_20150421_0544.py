# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0005_infoprediogeneral_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='acceso_predio_anio',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='altitud',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='area_arrendamiento',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='arecipitacion',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='coordenada_n',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='coordenada_w',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='ext_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='km_abecera_mpal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='medio_transporte_predio',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='nombre_predio',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='tenencia_finca',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='total_area_pastoreo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='total_banco_forraje',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='total_bosque',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='total_cultivo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='total_plantacion_forestal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='total_sistema_agroforestal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='total_uso_suelo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='utiliza_sabanas_comunales',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='viven_producido',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
