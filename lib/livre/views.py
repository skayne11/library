from django.shortcuts import render

from django.shortcuts import render
from .models import Livres

def livres(request):
    livre = Livres.objects.all()
    context = {
        'livres': livre
    }
    return render(request, 'livre.html', context)

