from django.contrib import admin

from computing.models import Computer, OperatingSystem, IPPolicy, Subnet


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ip', 'user', 'room', 'subnet')
#    fieldsets = [
#        (None,               {'fields': ['hostname']}),
#        ('Usage information', {'fields': ['user', 'purpose']}),
#        #('Usage information', {'fields': ['user'], 'classes': ['collapse']}),
#    ]


admin.site.register(Computer, ComputerAdmin)
admin.site.register(OperatingSystem)
admin.site.register(IPPolicy)
admin.site.register(Subnet)
