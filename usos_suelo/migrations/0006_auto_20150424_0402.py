# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0007_actividadecoturismo_atractivoecoturismo'),
        ('usos_suelo', '0005_auto_20150424_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cultivoagricola',
            name='tipo',
        ),
        migrations.AddField(
            model_name='cultivoagricola',
            name='tipo',
            field=models.ForeignKey(to='opciones.TipoSiembra', default=0),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='plantacionforestal',
            name='tipo',
        ),
        migrations.AddField(
            model_name='plantacionforestal',
            name='tipo',
            field=models.ForeignKey(to='opciones.TipoSiembra', default=0),
            preserve_default=False,
        ),
    ]
