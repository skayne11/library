from django.db import models

class Livre(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=50)
    description = models.TextField()
    image = models.TextField()
