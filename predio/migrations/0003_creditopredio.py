# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0002_auto_20150418_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditoPredio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('cantidad_predio', models.CharField(max_length=1)),
                ('origen_credito', models.CharField(max_length=100)),
                ('lugar_expedicion', models.CharField(max_length=100)),
                ('pago_cuota', models.IntegerField()),
                ('tipo_cuota', models.CharField(choices=[('Mensual', 'Mensual'), ('Semestral', 'Semestral')], max_length=30)),
                ('uso_principal', models.CharField(max_length=100)),
                ('posee_incentivo', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('tipo_incentivo', models.CharField(choices=[('ICR', 'Incentivo a la Capitalizacion Rural'), ('CIF', 'Certificado de Incentivo Agroforestal'), ('TDF', 'Tasa de Interes'), ('IAT', 'Incentivo de Asistencia Tecnica'), ('EP', 'Extension Predial'), ('Otro', 'Otro')], max_length=100)),
                ('ingresos_externos', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('posee_subsidio', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
    ]
