from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request, "index.html")


# 处理登录请求
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        #调用数据库用户名和密码进行
        user = auth.authenticate(
            username = username, password = password)
        print(user)
        print(type(user))
        if user is None:
            return render(request, 'index.html',
                            {'error': 'username or password error'})
        else:
            #return HttpResponse('success')
            response = HttpResponseRedirect('/home/')
            response.set_cookie('username', username, 3600)
            return response
    else:
        return render(request, 'index.html',
                        {'error': 'username or password error'})

def home(request):
    username = request.COOKIES.get('username', '')
    return render(request, 'home.html', {'username': username})

def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    #清除cookie里保存的username
    return response
