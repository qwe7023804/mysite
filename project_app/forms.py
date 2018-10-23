from django import forms
from django.forms import ModelForm
# from django.contrib import auth
# from django.contrib.auth.models import User
from .models import Project, Module

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, help_text='请输入您的用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

# class ProjectForm(forms.Form):
#     project_name = forms.CharField(label='项目名称', max_length=20)
#     project_status = forms.BooleanField(label='状态', required=False)
#     project_remarks = forms.CharField(label='项目描述', widget=forms.Textarea)

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        #fields 展示字段 exclude 不展示字段
        fields = ['project_name', 'project_status', 'project_remarks']

class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = ['module_name', 'project', 'module_describe']
