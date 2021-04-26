from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name='index'),
    path('music/', views.MusicListView.as_view(), name='music-list'),
    path('music/create', views.MusicCreateView.as_view(), name='music-create'),
]