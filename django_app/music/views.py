from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,  'music/index.html')


def genres(request):
    return render(request,  'music/genres.html')

def events(request):
    return render(request,  'music/events.html')

def listen(request):
    return render(request,  'music/listen.html')


def videos(request):
    return render(request,  'music/video.html')