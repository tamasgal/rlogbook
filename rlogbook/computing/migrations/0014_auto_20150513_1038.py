# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0013_auto_20150513_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rrzelicense',
            old_name='description',
            new_name='order_nr',
        ),
    ]
