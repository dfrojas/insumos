# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lacteos', '0002_otrosderivados'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comprador',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='otrosderivados',
            name='predio',
        ),
        migrations.AddField(
            model_name='produccionleche',
            name='dulces',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produccionleche',
            name='kumis',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produccionleche',
            name='mantequilla',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produccionleche',
            name='queso_cuajada',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produccionleche',
            name='queso_de_mano',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produccionleche',
            name='queso_maduro',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produccionleche',
            name='queso_prensado',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produccionleche',
            name='yogurth',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OtrosDerivados',
        ),
        migrations.AddField(
            model_name='produccionleche',
            name='a_quien_vende',
            field=models.ManyToManyField(to='lacteos.Comprador'),
        ),
    ]
