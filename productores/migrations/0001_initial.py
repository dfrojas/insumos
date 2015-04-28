# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opciones', '0003_estadocivil_genero_regimensalud_rolpersona_sisben_tipoidentificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('numero_identificacion', models.CharField(max_length=100)),
                ('primer_nombre', models.CharField(max_length=100)),
                ('segundo_nombre', models.CharField(max_length=100)),
                ('primer_apellido', models.CharField(max_length=100)),
                ('segundo_apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('lugar_nacimiento', models.CharField(max_length=100)),
                ('direccion_residencia', models.CharField(max_length=100)),
                ('estado_civil', models.ForeignKey(related_name='estado civil+', to='opciones.EstadoCivil')),
                ('extranjero', models.ForeignKey(related_name='extranjero+', to='opciones.Booleanos')),
                ('genero', models.ForeignKey(related_name='genero+', to='opciones.Genero')),
                ('regimen_salud', models.ForeignKey(related_name='regimen salud+', to='opciones.RegimenSalud')),
                ('rol', models.ForeignKey(to='opciones.RolPersona')),
                ('sisben', models.ForeignKey(related_name='sisben+', to='opciones.Sisben')),
                ('tipo_identificacion', models.ForeignKey(related_name='tipo identificacion+', to='opciones.TipoIdentificacion')),
            ],
        ),
    ]
