# music/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('playlist/create/', views.playlist_create, name='playlist_create'),
]
