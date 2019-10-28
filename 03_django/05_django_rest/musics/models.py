from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE) # related_name='musics'로 하면 music_set대신 사용가능. -> migration새로 해야함
    title = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content