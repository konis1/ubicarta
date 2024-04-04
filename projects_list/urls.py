from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projets", views.index, name="projects"),
    path("projet_<str:pk>/", views.project, name="project"),
    path("contact-us/", views.project, name="contact-us"),
]
