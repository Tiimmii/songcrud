from django.db import models

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=20)
    date_released = models.DateTimeField()
    likes = models.IntegerField()
    artist_id = models.IntegerField()
    artists = models.ForeignKey('Artist', on_delete=models.CASCADE)

class Lyric(models.Model):
    content = models.CharField(max_length = 2000)
    song_id = models.IntegerField()
    songs = models.OneToOneField('song', on_delete=models.CASCADE)
