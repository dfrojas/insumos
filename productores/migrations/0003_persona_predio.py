# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0004_viviendapredio'),
        ('productores', '0002_auto_20150419_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='predio',
            field=models.ForeignKey(default=0, related_name='predio+', to='predio.InfoPredioGeneral'),
            preserve_default=False,
        ),
    ]
