# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0002_auto_20141127_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='os',
            field=models.ForeignKey(blank=True, to='computing.OperatingSystem', null=True),
            preserve_default=True,
        ),
    ]
