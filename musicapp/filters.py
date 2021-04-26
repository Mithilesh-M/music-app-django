import django_filters
from .models import Music, Album, Band, Label, Genre

class MusicFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    slug = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Music
        fields = ['title','slug','album','band']