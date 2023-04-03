from django.shortcuts import render
from .models import Livre

def livre_index(request):
    livre = Livre.objects.all()
    context = {
        'livres': livre
    }
    return render(request, 'livre.html', context)

def livre_detail(request, pk):
    livre_det = Livre.objects.get(pk=pk)
    context = {
        'livres': livre_det
    }
    return render(request, 'livre_detail.html', context)