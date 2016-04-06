from django.db import models

# Create your models here.
from albums.models import Album
from artists.models import Artist

class Track(models.Model):
    title=models.CharField(max_length=255)
    order=models.PositiveIntegerField()
    track_file=models.FileField(upload_to='tracks')
    album=models.ForeignKey(Album)
    artist=models.ForeignKey(Artist)

    def player(self):
    	#return self.track_file.url
    	return """
    	<audio controls>
    		<source src="%s" type="audio/mpeg">
    		Your Browser dont suport the audio tag
    	</audio>
    	""" % self.track_file.url

    player.allow_tags = True
    player.admin_order_field = 'track_file'

    def __str__(self):
    	return str(self.title)
