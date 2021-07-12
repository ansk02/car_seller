from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):

	def thumbnail(self, object):
		return format_html('<img src=" {} " width="40" style="border-radius:50px;" />'.format(object.photo.url))

	thumbnail.short_description = 'Photo'

	list_display = ('lastname', 'firstname','designation', 'thumbnail')
	list_display_links = ('firstname', 'lastname', 'thumbnail')
	search_fields = ('lastname', 'firstname', 'designation')
	list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)