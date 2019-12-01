from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('genres', views.genres),
    path('events', views.events),
    path('listen', views.listen),
    path('videos', views.videos)

]