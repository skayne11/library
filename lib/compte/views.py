from django.shortcuts import render

from django.shortcuts import render
from .models import Comptes
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import UserForms


def compte(request):
    compte = Comptes.objects.all()
    context = {
        'comptes': compte
    }
    return render(request, 'comptes.html', context)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForms(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForms()

    return render(request, 'compte.html', {'form': form})
