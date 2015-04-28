# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0003_estadocivil_genero_regimensalud_rolpersona_sisben_tipoidentificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='AguaProduccion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('opcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AguaUsoDomestico',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('opcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SistemaSuccionAgua',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('opcion', models.CharField(max_length=100)),
            ],
        ),
    ]
