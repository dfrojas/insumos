# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0008_auto_20150421_0603'),
        ('opciones', '0005_tiposiembra'),
        ('usos_suelo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BancosForraje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('clasificacion_forraje', models.CharField(max_length=100)),
                ('area_cosecha', models.CharField(max_length=100)),
                ('anio_establecimiento', models.CharField(max_length=100)),
                ('rendimiento', models.CharField(max_length=100)),
                ('densidad_semillas', models.CharField(max_length=100)),
                ('tipo_semillas', models.CharField(max_length=100)),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral', related_name='nombre del predio+')),
            ],
        ),
        migrations.CreateModel(
            name='ConservacionNatural',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre_conservacion_natural', models.CharField(max_length=100)),
                ('area_cultivada', models.IntegerField()),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('area_cultivada', models.IntegerField()),
                ('area_cosechada', models.IntegerField()),
                ('anio_establecimiento', models.CharField(max_length=20)),
                ('rendimiento', models.CharField(max_length=20)),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
                ('tipo', models.ManyToManyField(to='opciones.TipoSiembra')),
            ],
        ),
        migrations.CreateModel(
            name='Pastoreo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('area', models.CharField(max_length=100)),
                ('clasificacion_pastoreo', models.CharField(max_length=100)),
                ('tipo_pastoreo', models.CharField(max_length=100)),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral', related_name='predio')),
            ],
        ),
        migrations.CreateModel(
            name='PlantacionForestal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre_plantacion', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=100)),
                ('area_cultivada', models.IntegerField()),
                ('area_cosechada', models.IntegerField()),
                ('anio_establecimiento', models.CharField(max_length=20)),
                ('rendimiento', models.CharField(max_length=20)),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
                ('tipo', models.ManyToManyField(to='opciones.TipoSiembra')),
            ],
        ),
    ]
