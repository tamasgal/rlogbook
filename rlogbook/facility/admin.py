from django.contrib import admin
from facility.models import Building, Room, Location, User


class UserAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(User, UserAdmin)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Location)



