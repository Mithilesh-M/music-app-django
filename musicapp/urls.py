from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name='index'),
    path('music/', views.MusicListView.as_view(), name='music-list'),
    path('music/create', views.MusicCreateView.as_view(), name='music-create'),
    path('music/update/<int:pk>', views.MusicUpdateView.as_view(), name='music-update'),
    path('music/delete/<int:pk>', views.MusicDeleteView.as_view(), name='music-delete'),
    path('music/detail/<int:pk>', views.MusicDetailView.as_view(), name='music-detail'),
]