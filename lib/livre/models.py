from django.db import models
from django.contrib.auth.models import User

class Livre(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=50)
    description = models.TextField()
    image = models.TextField()
    lu = models.BooleanField(default=False)

class Lecture(models.Model):
    # utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100, null=True)
    auteur = models.CharField(max_length=50, null=True)
    image = models.TextField(null=True)
    status_lecture = models.BooleanField(default=False)
