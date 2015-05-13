# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0011_computer_model_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='RRZELicense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='computer',
            name='rrze_licences',
            field=models.ManyToManyField(to='computing.RRZELicense'),
            preserve_default=True,
        ),
    ]
