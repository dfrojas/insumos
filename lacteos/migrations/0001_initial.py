# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0010_auto_20150422_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduccionLeche',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('total_producido_litro_dia', models.IntegerField()),
                ('cantidad_destinada_productos_lacteos', models.IntegerField()),
                ('cantidad_destinada_autoconsumo_dia', models.IntegerField()),
                ('precio_litro_leche', models.IntegerField()),
                ('promedio_vacas_ordenadas_dia', models.IntegerField()),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
    ]
