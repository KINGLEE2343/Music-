# music/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Song, Artist, Playlist
from django.contrib import messages

def index(request):
    songs = Song.objects.all()
    return render(request, 'music/index.html', {'songs': songs})

def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'music/song_detail.html', {'song': song})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'music/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'music/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('index')

@login_required
def playlist_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        playlist = Playlist.objects.create(user=request.user, name=name)
        return redirect('index')
    return render(request, 'music/playlist_create.html')
