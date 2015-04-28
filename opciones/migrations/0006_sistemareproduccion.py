# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0005_tiposiembra'),
    ]

    operations = [
        migrations.CreateModel(
            name='SistemaReproduccion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('opcion', models.CharField(max_length=100)),
            ],
        ),
    ]
