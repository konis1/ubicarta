from django.shortcuts import render
from .models import Project, Categorie, Feature

def index(request):
    projects = Project.objects.all()
    categories = Categorie.objects.all()
    context = { 'projects': projects, 'categories': categories}
    return render(request, 'projects.html', context)

def project(request, pk):
    project = Project.objects.get(id=pk)
    features = Feature.objects.all()
    context = {'project': project, 'features': features}
    return render(request, 'project.html', context)
