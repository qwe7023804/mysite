from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required

# Create your views here.https://sobooks.cc/books/10313.html#respond

def index(request):
    return render(request, "index.html")

# 处理登录请求

def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        #调用数据库用户名和密码进行
        user = authenticate(request, username = username, password = password)
        if user is not None:
            #return HttpResponse('success')
            login(request, user)
            response = HttpResponseRedirect('/home/')
            response.set_cookie('username', username, 3600)
            return response
        else:
            return render(request, 'index.html',
                {'error': 'username or password error'})
    else:
        return render(request, 'index.html')

def home(request):
    username = request.COOKIES.get('username', '')
    return render(request, 'home.html', {'username': username})

def logout_view(request):
    logout(request)
    #response = HttpResponseRedirect('/index/')
    #清除cookie里保存的username
    return render(request, 'index.html')
