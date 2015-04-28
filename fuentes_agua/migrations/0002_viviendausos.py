# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0004_aguaproduccion_aguausodomestico_sistemasuccionagua'),
        ('predio', '0004_viviendapredio'),
        ('fuentes_agua', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViviendaUsos',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('agua_produccion', models.ManyToManyField(to='opciones.AguaProduccion')),
                ('agua_uso_domestico', models.ManyToManyField(to='opciones.AguaUsoDomestico')),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
                ('sistema_succion_agua', models.ManyToManyField(to='opciones.SistemaSuccionAgua')),
            ],
        ),
    ]
