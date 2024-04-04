from django.shortcuts import get_object_or_404,render
from django_user_agents.utils import get_user_agent
from .models import Project, Categorie, Feature, Image

def index(request):
    projects = Project.objects.all()
    categories = Categorie.objects.all()
    context = { 'projects': projects, 'categories': categories}
    return render(request, 'projects.html', context)

def project(request, pk):
    project = get_object_or_404(Project, id=pk)
    features = Feature.objects.filter(feature_project=project)
    images = Image.objects.filter(project=project)
    user_agent = get_user_agent(request)

    if user_agent.is_mobile:
        if 'Android' in user_agent.os.family:
            device_type = 'android'
        else:
            device_type = 'apple'
    else:
        device_type = "desktop"

    context = {
        'project': project,
        'features': features,
        'device_type': device_type,
        'images': images
        }
    return render(request, 'project.html', context)

def home(request):
    # get project selected for home
    # get the main image for each project ?
    return render(request, 'home.html')

def contact_us(request):
    return render(request)
