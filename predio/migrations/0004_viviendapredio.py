# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0001_initial'),
        ('predio', '0003_creditopredio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViviendaPredio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('bateria_sanitaria', models.ForeignKey(to='opciones.Booleanos', related_name='booleanos+')),
                ('cubierta', models.ForeignKey(to='opciones.Cubierta', related_name='cubierta+')),
                ('energia_alternativa', models.ForeignKey(to='opciones.Booleanos', related_name='booleanos+')),
                ('energia_electrica', models.ForeignKey(to='opciones.Booleanos', related_name='booleanos+')),
                ('energia_preparacion_alimentos', models.ForeignKey(to='opciones.FuenteEnergiaPreparacionAlimentos', related_name='fuente energia+')),
                ('estado_saneamiento', models.ForeignKey(to='opciones.BMR', related_name='bueno malo regular+')),
                ('fuente_energia', models.ForeignKey(to='opciones.FuenteEnergia', related_name='fuente energia+')),
                ('posee_vivienda', models.ForeignKey(to='opciones.Booleanos', related_name='booleanos+')),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
                ('tipo_construccion', models.ForeignKey(to='opciones.TipoConstruccion', related_name='tipo construccion+')),
            ],
        ),
    ]
