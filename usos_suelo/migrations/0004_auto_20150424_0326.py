# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usos_suelo', '0003_auto_20150421_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pastoreo',
            name='area',
        ),
        migrations.RemoveField(
            model_name='pastoreo',
            name='clasificacion_pastoreo',
        ),
        migrations.RemoveField(
            model_name='pastoreo',
            name='tipo_pastoreo',
        ),
        migrations.AddField(
            model_name='pastoreo',
            name='arboles_dispersos_en_potreros',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pastoreo',
            name='cercas_vivas',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pastoreo',
            name='franjas_dobles_arboles_en_potreros',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pastoreo',
            name='pasturas_introducidas_sin_arboles',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pastoreo',
            name='pasturas_nativas_sin_arboles',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pastoreo',
            name='sistema_silvopastoril_intensivo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pastoreo',
            name='sistema_silvopastoril_intensivo_con_maderables',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
