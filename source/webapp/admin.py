from django.contrib import admin

# Register your models here.
from webapp.models import Photo, Album

admin.site.register(Photo)
admin.site.register(Album)

