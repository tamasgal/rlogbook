
# coding=utf-8
# Filename: read_xls.py
"""
Reads from an Excel file and imports/updates entries in the database.

"""
import sys
import os
sys.path.append('../rlogbook')
os.environ['DJANGO_SETTINGS_MODULE'] = 'rlogbook.settings'

import xlrd
import django
django.setup()

from computing.models import Computer, ComputerType, Subnet
from facility.models import User

file = '/Users/tamasgal/Desktop/Computing_List_2014_reformatted.xlsx'

book = xlrd.open_workbook(file)

print("Found {} sheet(s) in workbook:".format(book.nsheets))
for sheet_name in book.sheet_names():
    print(' '*5 + sheet_name)

mac_mini_sheet = book.sheet_by_name(u'Mac Minis')

print(mac_mini_sheet.ncols)
print(mac_mini_sheet.nrows)


header = []
for title in mac_mini_sheet.row_values(0):
    header.append(title)

def get_user(raw_entry):
    name = raw_entry.strip()
    if not name:
        return
    if ',' in name:
        lastname, firstname = name.split(',')
        name = u"{0} {1}".format(firstname.strip(), lastname.strip())
    users_in_db = User.objects.filter(name=name)
    if users_in_db:
        return users_in_db[0]
    else:
        user = User(name=name)
        user.save()
        return user


new_entries = 0
updated_entries = 0
for i in range(1, mac_mini_sheet.nrows):
    values = mac_mini_sheet.row_values(i)
    name = values[0].strip()
    if name.startswith('Mac Mini') and 'Server' not in name:
        computers_in_db = Computer.objects.filter(name=name)
        if computers_in_db:
            if len(computers_in_db) > 1:
                print("More than one entry for computer with name {}"
                      .format(name))
            computer = computers_in_db[0]
            updated_entries += 1
        else:
            computer = Computer()
            new_entries += 1
        computer.name = name
        computer.ip = values[2]
        computer.serial_number = values[3]
        computer.mac_address = values[4]
        computer.mac_airport = values[5]
        computer.mac_bluetooth = values[6]
        computer.computer_type = ComputerType.objects.filter(name='Mac Mini')[0]
        computer.subnet = Subnet.objects.filter(name='Arbeitsplätze')[0]
        computer.part_no = values[7]
        computer.user = get_user(values[8])
        computer.hostname = 'pi2' + name.split(' ')[2]
        computer.save()



print("New entries: {}".format(new_entries))
print("Updated entries: {}".format(updated_entries))
