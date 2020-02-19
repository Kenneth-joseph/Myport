from django.shortcuts import render, redirect
from django.http import Http404, HttpRequest, HttpResponse
from .models import Project, Profile, Rating
from .forms import NewProjectForm, UpdateUserForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    project = Project.get_project()
    return render(request, 'home.html', {"project": project})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "projects": searched_project})
    else:
        message = "You have made any search yet, please do to get the awesome projects"
        return render(request, 'search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            project.save()
        return redirect('home')
    else:
        form = NewProjectForm
    return render(request, 'new_project.html', {"form": form})


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='/accounts/login/')
def update_profile(request):
    u_form = UpdateUserForm()
    p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'update_profile.html', context)
