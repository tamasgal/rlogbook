# -*- coding: utf-8 -*-
# Filename: read_xls.py
"""
Change "First Last" to unix-login name. "Tamas Gal" -> tgal

"""
import sys
import os
sys.path.append('../rlogbook')
os.environ['DJANGO_SETTINGS_MODULE'] = 'rlogbook.settings'

import django
django.setup()

from facility.models import User

for user in User.objects.all():
    if ' ' in user.name and \
       not (user.name.startswith('in ')
            or user.name.startswith('frei ')
            or user.name.startswith('Zulassungsarbeit ')
            or user.name.startswith('HiWi ')
            or user.name.startswith('BSc ')):
        first, last = user.name.split(' ')
        new_name = first.lower()[0] + last.lower()
        new_name = new_name.replace(u'ä', u'ae')
        new_name = new_name.replace(u'ö', u'oe')
        new_name = new_name.replace(u'ü', u'ue')
        new_name = new_name.replace(u'ß', u'ss')
        
        print user.name + " -> " + new_name
        user.name = new_name
        user.save()

