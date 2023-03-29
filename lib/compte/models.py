from django.db import models

class Comptes(models.Model):
    title = models.CharField(max_length=100)
    auteur = models.CharField(max_length=25)
    description = models.TextField(max_length=500)
    image = models.FilePathField(path="/img")
