from datetime import datetime, timezone
import django
from django.db import models

# Create your models here.
class Artiste(models.Model): 
    first_name = models.CharField(max_length=200, blank= False,  null=True)
    last_name = models.CharField(max_length=200, blank= False,  null=True)
    age = models.IntegerField(default=0)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Artist'
        verbose_name_plural = 'Artistes'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Song(models.Model): 
    title = models.CharField(max_length=200, blank= False,  null=True)
    date_released = models.DateTimeField()
    likes = models.IntegerField(default=0)
    artiste_id = models.ForeignKey(Artiste, related_name='artist_detail', on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.title



class Lyric(models.Model): 
    content = models.CharField(max_length=2000, blank= False,  null=True)
    song_id = models.ForeignKey(Song, related_name='song_detail', on_delete=models.CASCADE)

    class Meta:
        ordering = ['song_id']
        verbose_name = 'lyric'
        verbose_name_plural = 'lyrics'

    def __str__(self):
        return self.song_id.title

