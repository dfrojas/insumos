# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0002_formaproteccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('opcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('opcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegimenSalud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('opcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RolPersona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('rol', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sisben',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('opcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoIdentificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('opcion', models.CharField(max_length=100)),
            ],
        ),
    ]
