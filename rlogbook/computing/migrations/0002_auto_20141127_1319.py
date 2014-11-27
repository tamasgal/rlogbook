# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='description',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='hostname',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='os',
            field=models.ForeignKey(to='computing.OperatingSystem', blank=True),
            preserve_default=True,
        ),
    ]
