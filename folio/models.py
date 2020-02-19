from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    phone_number = models.IntegerField(blank=True)
    profile_pic = models.ImageField(upload_to='pictures/', default='kent.jpg')
    email = models.EmailField()

    def __str__(self):
        return f'{self.user.username} profile'


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = HTMLField()
    project_link = models.CharField(max_length=100)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    project_pic = models.ImageField(upload_to='pictures/', default='kent.jpg')

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_project(cls):
        proj = Project.objects.all()
        return proj

    @classmethod
    def search_by_title(cls, search_term):
        work = cls.objects.filter(title__icontains=search_term)
        return work

    def __str__(self):
        return self.title


class Rating(models.Model):
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    project = models.ForeignKey(Project)

    def __str__(self):
        return self.content
# Create your models here.
