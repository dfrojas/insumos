# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0010_auto_20150422_1609'),
        ('manejo_finca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermadades',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EnfermedadesProblemasSanitariosFrecuentes',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('enfermedad', models.ManyToManyField(to='manejo_finca.Enfermadades')),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
        migrations.CreateModel(
            name='LaboresAnimal',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LaboresPracticadasAnimal',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('labor_practicada_a_animal', models.ManyToManyField(to='manejo_finca.LaboresAnimal')),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
        migrations.CreateModel(
            name='Vacunas',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VacunasAplicadaGanado',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
                ('vacuna', models.ManyToManyField(to='manejo_finca.Vacunas')),
            ],
        ),
    ]
