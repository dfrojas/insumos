# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('cantidad_ninos', models.IntegerField()),
                ('cantidad_ninas', models.IntegerField()),
                ('cantidad_adulto_masculino', models.IntegerField()),
                ('cantidad_adulto_femenino', models.IntegerField()),
                ('cantidad_adultos_mayores_masculino', models.IntegerField()),
                ('cantidad_adultos_mayores_femenino', models.IntegerField()),
                ('totalninos', models.IntegerField()),
                ('total_adultos', models.IntegerField()),
                ('total_adultos_mayores', models.IntegerField()),
                ('predio', models.ForeignKey(to='predio.Predio')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tipo_identificacion', models.CharField(choices=[('CC', 'Cedula Ciudadania'), ('NIT', 'NIT')], max_length=5)),
                ('numero_identificacion', models.CharField(max_length=20)),
                ('primer_nombre', models.CharField(max_length=30)),
                ('segundo_nombre', models.CharField(max_length=30)),
                ('primer_apellido', models.CharField(max_length=30)),
                ('segundo_apellido', models.CharField(max_length=30)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('fecha_nacimiento', models.DateField(max_length=10)),
                ('lugar_nacimiento', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion_residencia', models.CharField(max_length=50)),
                ('estad_civil', models.CharField(choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Union Libre', 'Union Libre')], max_length=50)),
                ('regimen_salud', models.CharField(max_length=30)),
                ('sisben', models.CharField(max_length=10)),
                ('extranjero', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RelacionPredioPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('persona', models.ForeignKey(to='productores.Persona', related_name='persona')),
                ('predio', models.ForeignKey(to='predio.Predio')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='relacionprediopersona',
            name='rol',
            field=models.ForeignKey(to='productores.Rol', related_name='rol'),
        ),
    ]
