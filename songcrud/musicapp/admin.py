from django.contrib import admin
from .models import *


# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_released', 'likes', 'artiste_id']


class LyricAdmin(admin.ModelAdmin):
    list_display = ['content', 'song_id']


class ArtisteAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age']


admin.site.register(Song, SongAdmin)
admin.site.register(Lyric, LyricAdmin)
admin.site.register(Artiste, ArtisteAdmin)

