# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lacteos', '0004_auto_20150424_0514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insumo',
            old_name='suplemento',
            new_name='insumo',
        ),
    ]
