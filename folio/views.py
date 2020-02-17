from django.shortcuts import render, redirect
from django.http import Http404, HttpRequest, HttpResponse
from .models import Project, Profile, Rating


# Create your views here.
def home(request):
    project = Project.get_project()
    return render(request, 'home.html', {"project": project})


def search_results(request):
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "projects": searched_project})
    else:
        message = "You have made any search yet, please do to get the awesome projects"
        return render(request, 'search.html', {"message":message})
