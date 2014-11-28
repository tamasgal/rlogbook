from django.contrib import admin

from computing.models import (Computer, OperatingSystem, IPPolicy, Subnet,
                              ComputerType)


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'name', 'computer_type', 'ip', 'user', 'room',
                    'subnet')
    fieldsets = [
        (None, {
            'fields': ('hostname', 'name', 'computer_type', 'ip', 'user', 'room',
                       'subnet'),
            }),
        ('Purpose', {
            'fields': ('purpose', 'prior_purpose'),
            'classes': ['collapse'],
            }),
        ('Networking', {
            'fields': ['mac_address', 'dns_cname', 'dns_hinfo_computer',
                       'ip_policy'],
            'classes': ['collapse'],
            }),
        ('Software', {
            'fields': ['os', 'software_licenses'],
            'classes': ['collapse'],
            }),
        ('Hardware', {
            'fields': ['serial_number'],
            'classes': ['collapse'],
            }),
        ('Misc', {
            'fields': ['expiration_date'],
            'classes': ['collapse'],
            }),
        ('Notes', {
            'fields': ['comment'],
            }),
        #('Usage information', {'fields': ['user'], 'classes': ['collapse']}),
    ]


admin.site.register(Computer, ComputerAdmin)
admin.site.register(ComputerType)
admin.site.register(OperatingSystem)
admin.site.register(IPPolicy)
admin.site.register(Subnet)
