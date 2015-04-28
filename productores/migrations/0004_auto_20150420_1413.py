# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productores', '0003_persona_predio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='direccion_residencia',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='estado_civil',
            field=models.ForeignKey(blank=True, related_name='estado civil+', null=True, to='opciones.EstadoCivil'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='extranjero',
            field=models.ForeignKey(blank=True, related_name='extranjero+', null=True, to='opciones.Booleanos'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='genero',
            field=models.ForeignKey(blank=True, related_name='genero+', null=True, to='opciones.Genero'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='lugar_nacimiento',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='numero_identificacion',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='primer_apellido',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='regimen_salud',
            field=models.ForeignKey(blank=True, related_name='regimen salud+', null=True, to='opciones.RegimenSalud'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='segundo_apellido',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='segundo_nombre',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='sisben',
            field=models.ForeignKey(blank=True, related_name='sisben+', null=True, to='opciones.Sisben'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tipo_identificacion',
            field=models.ForeignKey(blank=True, related_name='tipo identificacion+', null=True, to='opciones.TipoIdentificacion'),
        ),
    ]
