from django.contrib import admin
from facility.models import Building, Room, Location, User


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'arrival', 'departure']
    search_fields = ['name', 'arrival', 'departure']


admin.site.register(User, UserAdmin)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Location)



