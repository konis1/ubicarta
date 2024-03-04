from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="projects"),
    path("projet_<str:pk>/", views.project, name="project"),
]
