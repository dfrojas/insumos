# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0007_actividadecoturismo_atractivoecoturismo'),
        ('predio', '0008_auto_20150421_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agroecoturismo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('observaciones', models.TextField()),
                ('actividad', models.ManyToManyField(to='opciones.ActividadEcoturismo')),
                ('atractivo', models.ManyToManyField(to='opciones.AtractivoEcoturismo')),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
    ]
