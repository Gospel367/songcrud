from django.shortcuts import render
from django.views.generic import ListView
from .models import Artiste, Lyric, Song
from musicapp.serializers import SongSerializer, LyricSerializer, ArtisteSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'songs': reverse('song_list', request=request, format=format),
        'artistes': reverse('artist_list', request=request, format=format),
        'lyrics': reverse('lyric_list', request=request, format=format),
    })

class Home(ListView):
    model = Song
    template_name ='home.html'
    context_object_name = 'home_posts'
    
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['lyrics'] = Lyric.objects.all()
        context['artistes']= Artiste.objects.all()
        return context




class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ArtisteList(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer


class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer


class LyricList(generics.ListCreateAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer


class LyricDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer

