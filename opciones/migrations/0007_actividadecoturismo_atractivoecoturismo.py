# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0006_sistemareproduccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadEcoturismo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('opcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AtractivoEcoturismo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('opcion', models.CharField(max_length=100)),
            ],
        ),
    ]
