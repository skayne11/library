from django.db import models


class Home(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.FilePathField(path="img/")
