from django.contrib import admin

# Register your models here.
from rooms import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        'city',
        'price',
        'guests',
        'beds',
        'bedrooms',
        'baths',
        'check_in',
        'check_out',
        'instant_book'
    )

    list_filter = ('instant_book', 'city', 'country')

    search_fields = ('=city', '^host__username')