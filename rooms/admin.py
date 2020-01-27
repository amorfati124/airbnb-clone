from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType)
class IteamAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Amenity)
class IteamAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Facility)
class IteamAdmin(admin.ModelAdmin):
    pass


@admin.register(models.HouseRules)
class IteamAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
