from django.db import models
import datetime as dt
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    phone_number = models.IntegerField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    project_link = models.CharField(max_length=100)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)


class Rating(models.Model):
    design = models.CharField(max_length=30)
# Create your models here.
