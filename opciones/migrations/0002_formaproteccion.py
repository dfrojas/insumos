# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaProteccion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('opcion', models.CharField(max_length=100)),
            ],
        ),
    ]
