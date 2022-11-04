from django.db import models

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Song(models.Model):
    title = models.CharField(max_length=20)
    date_released = models.DateTimeField()
    likes = models.IntegerField()
    artist_id = models.ForeignKey('Artist', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.CharField(max_length = 2000)
    song_id = models.ForeignKey('song', on_delete=models.CASCADE, related_name='lyrics')
