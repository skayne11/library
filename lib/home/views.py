from django.shortcuts import render
from .models import Home

def home_index(request):
    home = Home.objects.all()
    context = {
        'homes': home
    }
    return render(request, 'home.html', context)
