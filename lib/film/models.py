from django.db import models

class Films(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    image = models.FilePathField(path="/img")
