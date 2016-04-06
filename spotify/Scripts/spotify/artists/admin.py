from django.contrib import admin

# Register your models here.
from .models import Artist

class ArtistAdmin (admin.ModelAdmin):
	search_fields=('fris_name','last_name')
admin.site.register(Artist,ArtistAdmin)
