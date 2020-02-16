from django.db import models
import datetime as dt
from django.contrib.auth.models import User


class Profile(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    bio = models.TextField()
    phone_number = models.IntegerField(blank=True)
    profile_pic = models.ImageField(upload_to='pictures/',default='kent.jpg')
    email = models.EmailField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    project_link = models.CharField(max_length=100)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    project_pic = models.ImageField(upload_to='pictures/', default='kent.jpg')

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title


class Rating(models.Model):
    design = models.IntegerField(max_length=30, default=0)
    usability = models.IntegerField(max_length=30, default=0)
    content = models.IntegerField(max_length=30, default=0)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.content
# Create your models here.
