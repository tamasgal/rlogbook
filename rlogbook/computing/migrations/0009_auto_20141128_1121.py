# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computing', '0008_auto_20141128_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('warranty_length', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='computer',
            name='additional_software',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='mac_airport',
            field=models.CharField(max_length=17, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='mac_bluetooth',
            field=models.CharField(max_length=17, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='netrestore_image',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='part_no',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='purchase_date',
            field=models.DateField(null=True, verbose_name=b'purchase date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='repair_log',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='standard_software',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='warranty_type',
            field=models.ForeignKey(blank=True, to='computing.Warranty', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='ip',
            field=models.GenericIPAddressField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subnet',
            name='from_ip',
            field=models.GenericIPAddressField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subnet',
            name='to_ip',
            field=models.GenericIPAddressField(),
            preserve_default=True,
        ),
    ]
