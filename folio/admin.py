from django.contrib import admin
from .models import Project, Profile, Rating

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Rating)

