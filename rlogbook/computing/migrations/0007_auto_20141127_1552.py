# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0006_auto_20141127_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='prior_purpose',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='purpose',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
