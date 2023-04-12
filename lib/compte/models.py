from django.db import models



class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)

    @classmethod
    def create(cls, username, password):
        user = cls(username=username, password=password)
        return user

