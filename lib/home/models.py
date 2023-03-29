from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.FilePathField(path="/img")
