# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0014_auto_20150513_1038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rrzelicense',
            options={'ordering': ('name', 'order_nr')},
        ),
        migrations.AddField(
            model_name='computer',
            name='inventory_number',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='ram',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
