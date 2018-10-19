from django import forms
from django.contrib import auth
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, help_text='请输入您的用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

class ProjectForm(forms.Form):
    project_name = forms.CharField(label='项目名称', max_length=20)
    project_status = forms.BooleanField(label='状态', required=False)
    project_remarks = forms.CharField(label='项目描述', widget=forms.Textarea)
