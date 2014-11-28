# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0009_auto_20141128_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer',
            old_name='warranty_type',
            new_name='warranty',
        ),
    ]
