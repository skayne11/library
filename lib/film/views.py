from django.shortcuts import render

from django.shortcuts import render
from .models import Films

def films(request):
    film = Films.objects.all()
    if request.method == "GET":
        titre = request.GET.get('recherche')
        if titre is not None:
            film = Films.objects.filter(titre__icontains=titre)
    return render(request, 'films.html', {'films': film})

def film_detail(request, pk):
    livre_det = Films.objects.get(pk=pk)
    context = {
        'films': livre_det
    }
    return render(request, 'film_detail.html', context)
