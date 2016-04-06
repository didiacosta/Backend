from django.db import models


# Create your models here.
class Artist(models.Model):
    fris_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255, blank=True)
    biography=models.TextField(blank=True)

    def __str__(self):
    	return str(self.fris_name)
