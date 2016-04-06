from django.contrib import admin

# Register your models here.
from .models import Track

class TrackAdmin (admin.ModelAdmin):
	list_display= ('artist','title','order','album','player', 'es_diomedez')
	list_filter =('artist','album')
	search_fields=('title','artist__fris_name','artist__last_name')
	list_editable =('title','album',)
	raw_id_fields =('artist',)

	def es_diomedez(self,obj):
		return obj.id==1

	es_diomedez.boolean = True

admin.site.register(Track,TrackAdmin)

