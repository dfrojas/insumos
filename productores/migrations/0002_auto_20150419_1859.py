# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0003_estadocivil_genero_regimensalud_rolpersona_sisben_tipoidentificacion'),
        ('productores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='rol',
        ),
        migrations.AddField(
            model_name='persona',
            name='rol',
            field=models.ManyToManyField(to='opciones.RolPersona'),
        ),
    ]
