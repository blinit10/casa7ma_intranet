from django.contrib import admin

from tvs.models import Room, Slide


# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    filter_horizontal = ['slides',]

admin.site.register(Slide)
admin.site.register(Room, RoomAdmin)