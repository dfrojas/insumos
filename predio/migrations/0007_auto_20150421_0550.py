# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0006_auto_20150421_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditopredio',
            name='cantidad_predio',
            field=models.CharField(null=True, blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='creditopredio',
            name='ingresos_externos',
            field=models.CharField(null=True, choices=[('Si', 'Si'), ('No', 'No')], blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='creditopredio',
            name='lugar_expedicion',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='creditopredio',
            name='origen_credito',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='creditopredio',
            name='pago_cuota',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='creditopredio',
            name='posee_incentivo',
            field=models.CharField(null=True, choices=[('Si', 'Si'), ('No', 'No')], blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='creditopredio',
            name='posee_subsidio',
            field=models.CharField(null=True, choices=[('Si', 'Si'), ('No', 'No')], blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='creditopredio',
            name='tipo_cuota',
            field=models.CharField(null=True, choices=[('Mensual', 'Mensual'), ('Semestral', 'Semestral')], blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='creditopredio',
            name='tipo_incentivo',
            field=models.CharField(null=True, choices=[('ICR', 'Incentivo a la Capitalizacion Rural'), ('CIF', 'Certificado de Incentivo Agroforestal'), ('TDF', 'Tasa de Interes'), ('IAT', 'Incentivo de Asistencia Tecnica'), ('EP', 'Extension Predial'), ('Otro', 'Otro')], blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='creditopredio',
            name='uso_principal',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
    ]
