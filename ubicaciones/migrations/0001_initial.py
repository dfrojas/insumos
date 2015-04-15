# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corregimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('codigo_corregimiento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('codigo_departamento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('codigo_municipio', models.CharField(max_length=100)),
                ('departamento', models.ForeignKey(to='ubicaciones.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('codigo_pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vereda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('codigo_vereda', models.CharField(max_length=100)),
                ('corregimiento', models.ForeignKey(to='ubicaciones.Corregimiento')),
                ('predio', models.ForeignKey(to='predio.Predio', related_name='predio')),
            ],
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(to='ubicaciones.Pais'),
        ),
        migrations.AddField(
            model_name='corregimiento',
            name='municipio',
            field=models.ForeignKey(to='ubicaciones.Municipio'),
        ),
    ]
