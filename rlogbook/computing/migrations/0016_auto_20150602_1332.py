# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0015_auto_20150521_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='rrze_licenses',
            field=models.ManyToManyField(to='computing.RRZELicense', null=True, blank=True),
            preserve_default=True,
        ),
    ]
