from django.shortcuts import render
from .models import Livre

def livre_index(request):
    livres = Livre.objects.all()
    if request.method == "GET":
        titre = request.GET.get('recherche')
        if titre is not None:
            livres = Livre.objects.filter(titre__icontains=titre)
    return render(request, 'livre.html', {'livres': livres})


def livre_detail(request, pk):
    livre_det = Livre.objects.get(pk=pk)
    context = {
        'livres': livre_det
    }
    return render(request, 'livre_detail.html', context)