from django.contrib import admin
from .models import Festival, Artist
# Register your models here.


class FestivalAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_name', 'last_year', 'youtube_chanel')


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage_name', 'is_active', 'first_name',
                    'last_name', 'contry_origin')


admin.site.register(Festival, FestivalAdmin)
admin.site.register(Artist, ArtistAdmin)
