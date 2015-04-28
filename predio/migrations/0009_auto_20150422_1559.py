# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0008_auto_20150421_0603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infoprediogeneral',
            old_name='km_abecera_mpal',
            new_name='km_cabecera_mpal',
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='utiliza_sabanas_comunales',
            field=models.ForeignKey(to='opciones.Booleanos', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infoprediogeneral',
            name='viven_producido',
            field=models.ForeignKey(to='opciones.Booleanos', default=1, related_name='viven del producido+'),
            preserve_default=False,
        ),
    ]
