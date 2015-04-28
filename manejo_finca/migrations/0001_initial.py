# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0006_sistemareproduccion'),
        ('predio', '0008_auto_20150421_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManejoGeneral',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('edad_cria', models.IntegerField()),
                ('cria_ternerno_macho', models.ForeignKey(to='opciones.Booleanos', related_name='booelanos+')),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
                ('realiza_chequeo', models.ForeignKey(to='opciones.Booleanos', related_name='booelanos+')),
                ('sistema_reproduccion', models.ForeignKey(to='opciones.SistemaReproduccion', related_name='sistema de reproduccion+')),
            ],
        ),
    ]
