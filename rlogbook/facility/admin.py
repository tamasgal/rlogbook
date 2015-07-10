from django.contrib import admin
from facility.models import Building, Room, Location, User


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'arrival', 'departure']
    search_fields = ['name', 'arrival', 'departure']
    list_filter = ['arrival', 'departure']

class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'building']
    list_filter = ['building']

admin.site.register(User, UserAdmin)
admin.site.register(Building)
admin.site.register(Room, RoomAdmin)
admin.site.register(Location)



