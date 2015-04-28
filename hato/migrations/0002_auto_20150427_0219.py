# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0011_creditopredio_nombre_pestana'),
        ('hato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GanadoHembras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('propios', models.IntegerField()),
                ('ajenos', models.IntegerField()),
                ('totales', models.IntegerField(blank=True, null=True)),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
        migrations.CreateModel(
            name='GanadoMachos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('propios', models.IntegerField(blank=True, null=True)),
                ('ajenos', models.IntegerField(blank=True, null=True)),
                ('totales', models.IntegerField(blank=True, null=True)),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
        migrations.CreateModel(
            name='Hembras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Machos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OtrasEspecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('propios', models.IntegerField(blank=True, null=True)),
                ('ajenos', models.IntegerField(blank=True, null=True)),
                ('totales', models.IntegerField(blank=True, null=True)),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
        migrations.CreateModel(
            name='ParametroProductivoCeba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('peso_inicial_ceba', models.IntegerField()),
                ('edad_ceba', models.IntegerField()),
                ('ganancia_diaria_peso', models.IntegerField()),
                ('tiempo_periodo_ceba', models.IntegerField()),
                ('carga_animal', models.IntegerField()),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
        migrations.CreateModel(
            name='ParametroProductivoDobleProposito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('peso_vaca_produccion', models.IntegerField(blank=True, null=True)),
                ('litro_vaca_dia', models.IntegerField()),
                ('duracion_lactancia', models.IntegerField()),
                ('dias_abiertos', models.IntegerField()),
                ('peso_cria_nacimiento', models.IntegerField()),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
        migrations.CreateModel(
            name='ParametroProductivoLevante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('peso_destete', models.IntegerField()),
                ('edad_levante', models.IntegerField()),
                ('peso_final_levante', models.IntegerField()),
                ('ganancia_diaria_peso', models.IntegerField()),
                ('tiempo_periodo_levante', models.IntegerField()),
                ('carga_animal', models.IntegerField()),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
        migrations.AddField(
            model_name='ganadomachos',
            name='tipo_animal',
            field=models.ForeignKey(related_name='animal+', blank=True, to='hato.Machos', null=True),
        ),
        migrations.AddField(
            model_name='ganadohembras',
            name='tipo_animal',
            field=models.ForeignKey(related_name='animal+', blank=True, to='hato.Hembras', null=True),
        ),
    ]
