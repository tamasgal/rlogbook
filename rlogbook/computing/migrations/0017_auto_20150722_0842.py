# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0016_auto_20150602_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('from_ip', models.GenericIPAddressField()),
                ('to_ip', models.GenericIPAddressField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='computertype',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='ippolicy',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='operatingsystem',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='subnet',
            options={'ordering': ('sector', 'name')},
        ),
        migrations.AlterModelOptions(
            name='warranty',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='subnet',
            name='sector',
            field=models.ForeignKey(to='computing.Sector', null=True),
        ),
    ]
