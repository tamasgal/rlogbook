# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0002_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'ordering': ('name', 'acronym')},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ('room',)},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ('building', 'room_number')},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('name', 'arrival', 'departure')},
        ),
        migrations.AddField(
            model_name='user',
            name='arrival',
            field=models.DateField(null=True, verbose_name=b'arrival date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='departure',
            field=models.DateField(null=True, verbose_name=b'departure date', blank=True),
            preserve_default=True,
        ),
    ]
