# music/admin.py
from django.contrib import admin
from .models import Artist, Song, Playlist

admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Playlist)
# my_music_app/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
