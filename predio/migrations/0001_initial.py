# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre_predio', models.CharField(max_length=30)),
                ('coordenada_n', models.CharField(max_length=20)),
                ('coordenada_w', models.CharField(max_length=20)),
                ('ext_total', models.IntegerField()),
                ('area_arrendamiento', models.IntegerField()),
                ('altitud', models.IntegerField()),
                ('arecipitacion', models.IntegerField()),
                ('km_abecera_mpal', models.IntegerField()),
                ('acceso_predio_anio', models.CharField(max_length=10)),
                ('medio_transporte_predio', models.CharField(max_length=10)),
                ('tenencia_finca', models.CharField(max_length=3)),
                ('utiliza_sabanas_comunales', models.CharField(max_length=2)),
                ('viven_producido', models.CharField(max_length=2)),
                ('total_area_pastoreo', models.IntegerField()),
                ('total_banco_forraje', models.IntegerField()),
                ('total_bosque', models.IntegerField()),
                ('total_cultivo', models.IntegerField()),
                ('total_plantacion_forestal', models.IntegerField()),
                ('total_sistema_agroforestal', models.IntegerField()),
                ('total_uso_suelo', models.IntegerField()),
            ],
        ),
    ]
