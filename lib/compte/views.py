from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .form import CustomUserCreationForm
from .models import User

def register(request):
    print('tutu')
    register = CustomUserCreationForm()  # Inclure le formulaire dans le contexte de rendu

    if request.method == 'POST':
        if 'register_form' in request.POST:
            register = CustomUserCreationForm(request.POST)
            if register.is_valid():
                user = User()
                user.username = request.POST['username']
                user.password = request.POST['password1']
                user.password = make_password(user.password)
                user.save()
                return redirect('home')
    return render(request, 'comptes.html', {'register': register})
