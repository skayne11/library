from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Nom d\'utilisateur', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmation de mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    interet = forms.ChoiceField(label='Centre d\'intérêt', choices=(("1", "Livre"), ("2", "Film"), ("3", "Les deux")))
