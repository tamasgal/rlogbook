# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0003_auto_20150429_0918'),
        ('computing', '0017_auto_20150722_0842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manufacturer', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('printer_type', models.CharField(max_length=1, choices=[(b'0', b'laser'), (b'1', b'ink-jet'), (b'2', b'dot-matrix'), (b'3', b'lcd/led'), (b'4', b'thermal')])),
                ('color', models.BooleanField()),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('inventory_number', models.CharField(max_length=200, null=True, blank=True)),
                ('serial_number', models.CharField(max_length=200, null=True, blank=True)),
                ('mac_address', models.CharField(max_length=17, null=True, blank=True)),
                ('dns_cname', models.CharField(max_length=200, null=True, blank=True)),
                ('dns_hinfo_computer', models.CharField(max_length=200, null=True, blank=True)),
                ('hostname', models.CharField(max_length=200, null=True, blank=True)),
                ('purpose', models.TextField(null=True, blank=True)),
                ('prior_purpose', models.TextField(null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('ip', models.GenericIPAddressField(null=True, blank=True)),
                ('repair_log', models.TextField(null=True, blank=True)),
                ('purchase_date', models.DateField(null=True, verbose_name=b'purchase date', blank=True)),
                ('ip_policy', models.ForeignKey(blank=True, to='computing.IPPolicy', null=True)),
                ('room', models.ForeignKey(blank=True, to='facility.Room', null=True)),
                ('subnet', models.ForeignKey(blank=True, to='computing.Subnet', null=True)),
                ('user', models.ForeignKey(blank=True, to='facility.User', null=True)),
                ('warranty', models.ForeignKey(blank=True, to='computing.Warranty', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='computer',
            name='rrze_licenses',
            field=models.ManyToManyField(to='computing.RRZELicense', blank=True),
        ),
    ]
