from django.shortcuts import render

from django.shortcuts import render
from .models import Films

def films(request):
    film = Films.objects.all()
    context = {
        'films': film
    }
    return render(request, 'films.html', context)

def film_detail(request, pk):
    livre_det = Films.objects.get(pk=pk)
    context = {
        'films': livre_det
    }
    return render(request, 'film_detail.html', context)
