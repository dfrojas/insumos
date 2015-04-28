# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0008_auto_20150421_0603'),
        ('opciones', '0007_actividadecoturismo_atractivoecoturismo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnfoqueDiferencial',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('observaciones', models.TextField()),
                ('es_victima', models.ForeignKey(to='opciones.Booleanos', related_name='es victima+')),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
    ]
