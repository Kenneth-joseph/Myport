from django.db import models
import datetime as dt
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    phone_number = models.IntegerField(blank=True)
    email =models.EmailField()

# Create your models here.
