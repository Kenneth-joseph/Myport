from .models import Project
from django import forms
from .models import Profile
from django.contrib.auth.models import User


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','phone_number','profile_pic']
  
