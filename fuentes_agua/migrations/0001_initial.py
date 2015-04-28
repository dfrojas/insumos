# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0002_formaproteccion'),
        ('predio', '0004_viviendapredio'),
    ]

    operations = [
        migrations.CreateModel(
            name='NacimientosAgua',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cantidad_corrientes', models.IntegerField()),
                ('cantidad_zonas_rurales', models.IntegerField()),
                ('forma_proteccion', models.ForeignKey(to='opciones.FormaProteccion', related_name='forma proteccion agua+')),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
                ('protege_corrientes', models.ForeignKey(to='opciones.Booleanos', related_name='booleanos+')),
            ],
        ),
    ]
