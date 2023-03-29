from django.shortcuts import render

from django.shortcuts import render
from .models import Comptes

def compte(request):
    compte = Comptes.objects.all()
    context = {
        'comptes': compte
    }
    return render(request, 'comptes.html', context)
