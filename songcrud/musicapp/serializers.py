from rest_framework import serializers
from .models import Song, Lyric, Artiste



class SongSerializer(serializers.ModelSerializer):
    song_detail = serializers.PrimaryKeyRelatedField(many=True, queryset=Lyric.objects.all())

    class Meta:
        model = Song
        fields = ['title', 'date_released', 'likes', 'artiste_id', 'song_detail']


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['content', 'song_id']


class ArtisteSerializer(serializers.ModelSerializer):
    artist_detail = serializers.PrimaryKeyRelatedField(many=True, queryset=Song.objects.all())

    class Meta:
        model = Artiste
        fields = ['first_name', 'last_name', 'age', 'artist_detail']

