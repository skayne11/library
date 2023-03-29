from django.urls import path
from . import views

urlpatterns = [
    path("", views.livres, name="livre"),
]