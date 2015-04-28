# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usos_suelo', '0004_auto_20150424_0326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bancosforraje',
            name='anio_establecimiento',
        ),
        migrations.RemoveField(
            model_name='bancosforraje',
            name='area_cosecha',
        ),
        migrations.RemoveField(
            model_name='bancosforraje',
            name='clasificacion_forraje',
        ),
        migrations.RemoveField(
            model_name='bancosforraje',
            name='densidad_semillas',
        ),
        migrations.RemoveField(
            model_name='bancosforraje',
            name='rendimiento',
        ),
        migrations.RemoveField(
            model_name='bancosforraje',
            name='tipo_semillas',
        ),
        migrations.AddField(
            model_name='bancosforraje',
            name='bancos_energia',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bancosforraje',
            name='bancos_mixtos',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bancosforraje',
            name='bancos_proteina',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
