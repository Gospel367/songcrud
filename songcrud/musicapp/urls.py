from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from musicapp import views

urlpatterns = format_suffix_patterns([
    path('api', views.api_root),
    path('', views.Home.as_view(), name= 'homeview'),
    path('api/songs/', views.SongList.as_view(), name= 'song_list'),
    path('api/songs/<int:pk>/', views.SongDetail.as_view(), name= 'song_detail'),
    path('api/artistes/', views.ArtisteList.as_view(), name = "artist_list"),
    path('api/artistes/<int:pk>/', views.ArtisteDetail.as_view(), name = "artist_detail"),
    path('api/lyrics/', views.LyricList.as_view(), name ='lyric_list'),
    path('api/lyrics/<int:pk>/', views.LyricDetail.as_view(), name='lyric_detail'),

])



