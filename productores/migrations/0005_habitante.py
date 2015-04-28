# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0008_auto_20150421_0603'),
        ('productores', '0004_auto_20150420_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitante',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cantidad_ninos', models.IntegerField()),
                ('cantidad_ninas', models.IntegerField()),
                ('cantidad_adultos_masculino', models.IntegerField()),
                ('cantidad_adultos_femenino', models.IntegerField()),
                ('cantidad_adultos_mayores_masculino', models.IntegerField()),
                ('cantidad_adultos_mayores_femenino', models.IntegerField()),
                ('total_ninos', models.IntegerField(null=True, blank=True)),
                ('total_adultos', models.IntegerField(null=True, blank=True)),
                ('total_adultos_mayores', models.IntegerField(null=True, blank=True)),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
    ]
