from django.shortcuts import render

from django.shortcuts import render
from .models import Films

def films(request):
    film = Films.objects.all()
    context = {
        'films': film
    }
    return render(request, 'films.html', context)
