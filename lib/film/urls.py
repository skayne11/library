from django.urls import path
from . import views

urlpatterns = [
    path("", views.films, name="film"),
    path("<int:pk>/", views.film_detail, name="film_detail"),
]