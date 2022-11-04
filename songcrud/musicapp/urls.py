from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.artistelist),
    path('artists/<int:pk>/', views.artist_detail),
    path('songs/', views.songlist),
    path('songs/<int:pk>/', views.song_detail),
    path('lyrics/', views.lyriclist),
    path('lyrics/<int:pk>/', views.lyric_detail),
]