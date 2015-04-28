# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0010_auto_20150422_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditopredio',
            name='nombre_pestana',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
