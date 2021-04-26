from django.shortcuts import render
from .models import Music, Album, Band, Label, Genre


def show_index(request):
    context = {
        'No_Of_Music': Music.objects.all().count(),
        'No_Of_Album': Album.objects.all().count(),
        'No_Of_Band': Band.objects.all().count(),
        'No_Of_Label': Label.objects.all().count(),
        'No_Of_Genre': Genre.objects.all().count(),
    }
    return render(request, 'musicapp/index.html', context)
