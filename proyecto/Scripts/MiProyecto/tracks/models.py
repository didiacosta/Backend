from django.db import models
from albums.models import Album
from artists.models import Artist

# Create your models here.
class Track(models.Model):
    title=models.CharField(max_length=255)
    order=models.PositiveIntegerField()
    track_file=models.FileField(upload_to='tracks')
    album=models.ForeignKey(Album)
    artist=models.ForeignKey(Artist)

    def __str__(self):
    	return str(self.title)
