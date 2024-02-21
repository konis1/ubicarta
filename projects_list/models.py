from django.db import models

class Project(models.Model):
    title = models.CharField(max_length = 300)
    summary = models.CharField(max_length = 500)
    start_date = models.DateField()
    end_date = models.DateField()
    technologies_used = models.CharField(max_length = 300)
    challenges = models.TextField()
    solutions = models.TextField()
    future_directions = models.TextField()
    def __str__(self):
        return self.title

class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media")
    description = models.TextField()

class ProjectLink(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    url = models.URLField()
    description = models.TextField()

class Categorie(models.Model):
    name = models.CharField(max_length = 300)
    description = models.TextField()
    def __str__(self):
        return self.name
