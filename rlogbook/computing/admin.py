from django.contrib import admin

from computing.models import (Computer, OperatingSystem, IPPolicy, Subnet,
                              Sector, RRZELicense, ComputerType, Warranty)


class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_ip', 'to_ip')

class SubnetAdmin(admin.ModelAdmin):
    list_display = ('name', 'sector', 'from_ip', 'to_ip')

class PrinterAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'name', 'purpose', 'printer_type', 'model',
                    'ip', 'color', 'manufacturer', 'user', 'room', 'subnet')
    list_filter = ('printer_type', 'model', 'color', 'manufacturer', 'room',
                   'subnet')
    search_fields = ['name', 'hostname', 'purpose']

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'name', 'purpose', 'computer_type', 'ip',
                    'user', 'room', 'subnet', 'inventory_number', 'ram',
                    'comment')
    list_filter = ('computer_type', 'subnet', 'room')
    filter_horizontal = ('rrze_licenses',)
    search_fields = ['name', 'hostname']
    fieldsets = [
        (None, {
            'fields': ('hostname', 'name', 'computer_type', 'ip', 'user',
                       'room', 'subnet', 'inventory_number'),
            }),
        ('Purpose', {
            'fields': ('purpose', 'prior_purpose'),
            'classes': ['collapse'],
            }),
        ('Networking', {
            'fields': ['mac_address', 'mac_airport', 'mac_bluetooth',
                       'dns_cname', 'dns_hinfo_computer', 'ip_policy'],
            'classes': ['collapse'],
            }),
        ('Software', {
            'fields': ['os', 'standard_software', 'additional_software',
                       'software_licenses', 'rrze_licenses'],
            'classes': ['collapse'],
            }),
        ('Hardware', {
            'fields': ['serial_number', 'ram'],
            'classes': ['collapse'],
            }),
        ('Apple specific information', {
            'fields': ['part_no', 'netrestore_image', 'model_year'],
            'classes': ['collapse'],
            }),
        ('Purchase and warranty information', {
            'fields': ['purchase_date', 'warranty'],
            'classes': ['collapse'],
            }),
        ('Misc', {
            'fields': ['expiration_date'],
            'classes': ['collapse'],
            }),
        ('Notes', {
            'fields': ['repair_log', 'comment'],
            }),
    ]


admin.site.register(Computer, ComputerAdmin)
admin.site.register(ComputerType)
admin.site.register(OperatingSystem)
admin.site.register(IPPolicy)
admin.site.register(RRZELicense)
admin.site.register(Subnet, SubnetAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Warranty)




