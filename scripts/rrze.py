# -*- coding: utf-8 -*-
# Filename: rrze.py
"""
Reads in a text file containing RRZE licenses and adds/updates the entries in
the database.

The text file should have the following syntax:

    ORDER_NR
    DESCRIPTION
    ORDER_NR
    DESCRIPTION
    ...
    ...

"""
import sys
import os
sys.path.append('../rlogbook')
os.environ['DJANGO_SETTINGS_MODULE'] = 'rlogbook.settings'

import django
django.setup()

from computing.models import RRZELicense


with open('rrze.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    names = lines[1::2]
    order_nr = lines[::2]
    licenses = zip(names, order_nr)

for name, order_nr in licenses:
    rrze_licenses = RRZELicense.objects.filter(order_nr=order_nr) 
    if rrze_licenses:
        print("Skipping '{0}'".format(name))
        continue
    print("Adding new license: {0}".format(name))
    license = RRZELicense()
    license.name = name
    license.order_nr = order_nr
    license.save()

