from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from django.contrib import messages
from project_app.forms import LoginForm
# Create your views here.https://sobooks.cc/books/10313.html#respond

def index(request):
    return render(request, "Login.html")

#注册
# def registe(request):
#     return render(request, 'Login.html')

# 处理登录请求
def login_action(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/api/home/')
    login_form = LoginForm(request.POST.dict() or None)
    if request.method == 'POST' and login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            response = HttpResponseRedirect('/api/home/')
            return response
        else:
            messages.error(request, 'username or password error')
            return render(request, 'Home.html')
    return render(request, 'Login.html', {'login_form': login_form})


#退出
def logout_view(request):
    logout(request)
    #清除cookie里保存的username
    return render(request, 'Login.html')
