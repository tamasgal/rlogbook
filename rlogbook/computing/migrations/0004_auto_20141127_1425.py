# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0002_location'),
        ('computing', '0003_auto_20141127_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IPPolicy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='computer',
            name='description',
        ),
        migrations.AddField(
            model_name='computer',
            name='comment',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='dns_cname',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='dns_hinfo_computer',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='expiration_date',
            field=models.DateTimeField(null=True, verbose_name=b'expiration date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='ip',
            field=models.CharField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='ip_policy',
            field=models.ForeignKey(blank=True, to='computing.IPPolicy', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='mac_address',
            field=models.CharField(max_length=17, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='prior_purpose',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='purpose',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='serial_number',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='software_licenses',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='user',
            field=models.ForeignKey(blank=True, to='facility.User', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='hostname',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
