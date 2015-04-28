# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BMR',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('opcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Booleanos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('opcion', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Cubierta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('opcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FuenteEnergia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('opcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FuenteEnergiaPreparacionAlimentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('opcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoConstruccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('opcion', models.CharField(max_length=30)),
            ],
        ),
    ]
