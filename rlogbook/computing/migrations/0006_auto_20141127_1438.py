# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0005_auto_20141127_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='room',
            field=models.ForeignKey(blank=True, to='facility.Room', null=True),
            preserve_default=True,
        ),
    ]
