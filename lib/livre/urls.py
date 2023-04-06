from django.urls import path
from . import views

urlpatterns = [
    path("", views.livre_index, name="livre"),
    path("<int:pk>/", views.livre_detail, name="livre_detail"),
]