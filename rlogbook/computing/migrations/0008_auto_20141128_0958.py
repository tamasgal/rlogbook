# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0007_auto_20141127_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='computer',
            name='computer_type',
            field=models.ForeignKey(blank=True, to='computing.ComputerType', null=True),
            preserve_default=True,
        ),
    ]
