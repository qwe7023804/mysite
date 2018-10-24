from django import forms
from .models import Project, Module


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']

class ModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        exclude = ['create_time']
