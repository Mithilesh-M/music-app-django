from django.contrib import admin
from .models import Music,Album,Band,Label,Genre

admin.site.register(Music)
admin.site.register(Album)
admin.site.register(Band)
admin.site.register(Label)
admin.site.register(Genre)