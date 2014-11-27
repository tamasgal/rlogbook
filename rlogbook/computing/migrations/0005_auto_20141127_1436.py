# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0004_auto_20141127_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subnet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('from_ip', models.CharField(max_length=15)),
                ('to_ip', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='computer',
            name='subnet',
            field=models.ForeignKey(blank=True, to='computing.Subnet', null=True),
            preserve_default=True,
        ),
    ]
