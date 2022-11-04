from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.ArtisteList.as_view()),
    path('artists/<int:pk>/', views.ArtisteDetail.as_view()),
    path('songs/', views.SongList.as_view()),
    path('songs/<int:pk>/', views.SongDetail.as_view()),
    path('lyrics/', views.LyricList.as_view()),
    path('lyrics/<int:pk>/', views.LyricDetail.as_view()),
]