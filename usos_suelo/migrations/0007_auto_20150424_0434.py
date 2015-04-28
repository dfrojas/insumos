# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0010_auto_20150422_1609'),
        ('usos_suelo', '0006_auto_20150424_0402'),
    ]

    operations = [
        migrations.CreateModel(
            name='BosquesAreasConservacion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('area_regeneracion_natural', models.IntegerField()),
                ('area_cultivada', models.IntegerField()),
                ('matas_monte', models.IntegerField()),
                ('morichal', models.IntegerField()),
                ('estereo', models.IntegerField()),
                ('raudal', models.IntegerField()),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
        migrations.RemoveField(
            model_name='conservacionnatural',
            name='predio',
        ),
        migrations.DeleteModel(
            name='ConservacionNatural',
        ),
    ]
