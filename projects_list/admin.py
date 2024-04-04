from django.contrib import admin

# Register your models here.
from .models import Project, Image, ProjectLink, Categorie, Feature

admin.site.register(Categorie)
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(ProjectLink)
admin.site.register(Feature)
