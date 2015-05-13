# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0012_auto_20150513_1015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer',
            old_name='rrze_licences',
            new_name='rrze_licenses',
        ),
    ]
