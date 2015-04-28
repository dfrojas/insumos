# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0010_auto_20150422_1609'),
        ('lacteos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtrosDerivados',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('mantequilla', models.IntegerField()),
                ('yogurth', models.IntegerField()),
                ('kumis', models.IntegerField()),
                ('dulces', models.IntegerField()),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
    ]
