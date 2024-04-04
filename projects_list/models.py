from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length = 300)
    description = models.TextField()
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length = 300)
    summary = models.CharField(max_length = 500)
    start_date = models.DateField()
    end_date = models.DateField()
    technologies_used = models.CharField(max_length = 300)
    challenges = models.TextField()
    solutions = models.TextField()
    future_directions = models.TextField()
    on_homepage = models.BooleanField(default = False)
    description_image = models.ImageField(upload_to="static/media")
    project_category = models.ForeignKey(Categorie, on_delete=models.PROTECT, default = Categorie.objects.first().id)

    def __str__(self):
        return self.title

class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/media")
    description = models.TextField()

class ProjectLink(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    url = models.URLField()
    description = models.TextField()

class Feature(models.Model):
    feature_name = models.CharField(max_length = 300)
    feature_description = models.TextField()
    feature_image = models.ImageField(upload_to="static/media/feature", null=True)
    feature_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.feature_name
