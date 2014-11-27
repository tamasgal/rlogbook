from django.contrib import admin
from facility.models import Building, Room, Location, User
from computing.models import Computer, OperatingSystem

admin.site.register(Building)
admin.site.register(Room)
admin.site.register(User)
admin.site.register(Location)

admin.site.register(Computer)
admin.site.register(OperatingSystem)

