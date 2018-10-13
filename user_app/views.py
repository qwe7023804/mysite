from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from django.utils import timezone
# Create your views here.https://sobooks.cc/books/10313.html#respond

def index(request):
    return render(request, "Index.html")

# 处理登录请求
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #调用数据库用户名和密码进行
        user = authenticate(request, username = username, password = password)
        if user is not None:
            #登录状态
            login(request, user)
            response = HttpResponseRedirect('/api/home/')
            request.session['user'] = username
            return response
        else:
            return render(request, 'Index.html',
                {'error': 'username or password error'})
    else:
        return render(request, 'Index.html')



#创建项目页
@login_required
def create_project(request):
    username = request.session.get('user', '')
    time_now = timezone.now()
    return render(request, 'Create_Project.html', {'username': username,
                                                    'time_now': time_now})

#退出
def logout_view(request):
    logout(request)
    #清除cookie里保存的username
    return render(request, 'Index.html')
