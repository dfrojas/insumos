# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0004_aguaproduccion_aguausodomestico_sistemasuccionagua'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSiembra',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('opcion', models.CharField(max_length=100)),
            ],
        ),
    ]
