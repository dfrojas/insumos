# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0008_auto_20150421_0603'),
        ('opciones', '0005_tiposiembra'),
        ('usos_suelo', '0002_bancosforraje_conservacionnatural_cultivo_pastoreo_plantacionforestal'),
    ]

    operations = [
        migrations.CreateModel(
            name='CultivoAgricola',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
        migrations.RemoveField(
            model_name='cultivo',
            name='predio',
        ),
        migrations.RemoveField(
            model_name='cultivo',
            name='tipo',
        ),
        migrations.DeleteModel(
            name='Cultivo',
        ),
    ]
