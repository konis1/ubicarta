from django.shortcuts import render
from .models import Project, Categorie

def index(request):
    projects = Project.objects.all()
    categories = Categorie.objects.all()
    context = { 'projects': projects, 'categories': categories}
    return render(request, 'projects.html', context)
