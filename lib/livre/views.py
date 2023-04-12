from django.shortcuts import render
from .models import Lecture, Livre

def livre_index(request):
    livres = Livre.objects.all()
    if request.method == "GET":
        titre = request.GET.get('recherche')
        if titre is not None:
            livres = Livre.objects.filter(titre__icontains=titre)
    return render(request, 'livre.html', {'livres': livres})


def livre_detail(request, pk):
    global livre_lu
    livre_det = Livre.objects.get(pk=pk)
    if request.method == 'POST':
        livre_lu = request.POST['livre_lu']
        print(f"Livre lu : {livre_lu}")
        if livre_lu == 'on':
            livre_det.lu = True
            livre_det.save()
            print("Le livre est update !")
            titre = livre_det.titre
            auteur = livre_det.auteur
            image = livre_det.image
            lecture = Lecture(titre=titre, auteur=auteur, image=image)
            lecture.save()
        else:
            print("Le livre n'est pas lu")

    context = {
        'livres': livre_det
    }
    return render(request, 'livre_detail.html', context)

def livre_lu(request):
    lu = Lecture.objects.all()
    context = {
        'lu': lu
    }
    return render(request, 'mylibrary.html', context)



