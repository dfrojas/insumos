# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0010_auto_20150422_1609'),
        ('lacteos', '0003_auto_20150424_0501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('valor_unitario', models.IntegerField()),
                ('valor_total', models.IntegerField()),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
        migrations.CreateModel(
            name='Suplemento',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('valor_unitario', models.IntegerField()),
                ('valor_total', models.IntegerField()),
                ('predio', models.ForeignKey(to='predio.InfoPredioGeneral')),
            ],
        ),
        migrations.CreateModel(
            name='TipoInsumo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSuplemento',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='suplemento',
            name='suplemento',
            field=models.ForeignKey(to='lacteos.TipoSuplemento', related_name='suplemento+'),
        ),
        migrations.AddField(
            model_name='insumo',
            name='suplemento',
            field=models.ForeignKey(to='lacteos.TipoInsumo', related_name='insumos+'),
        ),
    ]
