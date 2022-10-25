from django.shortcuts import render
from django.views.generic import ListView
from .models import Artiste, Lyric, Song

# Create your views here.

class Home(ListView):
    model = Song
    template_name ='home.html'
    context_object_name = 'home_posts'
    
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['lyrics'] = Lyric.objects.all()
        context['artistes']= Artiste.objects.all()
        return context
