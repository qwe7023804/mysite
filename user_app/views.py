from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# 首页
def index(request):
    return render(request, "index.html")

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/manage/project_manage/')
    elif request.method == "POST":
        username = request.POST.get("username", '')
        email = request.POST.get('email', '18630146437@mail.com')
        password2 = request.POST.get("password2", '')
        password3 = request.POST.get("password3", '')
        if password2 != password3:  # 判断两次密码是否相同
            return render(request, 'index.html', {'message': '两次输入的密码不同！'})
        else:
            user = User.objects.create_user(username=username,
                                            email='18630146437@mail.com',
                                            is_staff=1,
                                            password=password2)
            user.save()
            return render(request, 'index.html', {'message': '注册成功'})  # 自动跳转到登录页面


# 处理登录请求
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if username == "" or password == "":
            return render(request, "index.html",
                          {"error": "用户名或者密码为空"}
                         )
        else:
            user = auth.authenticate(username=username, password=password)  # 验证用户是不是存在

            if user is not None:
                login(request, user) #记录用户登录状态
                request.session['user1'] = username
                return HttpResponseRedirect('/manage/project_manage/')
            else:
                return render(request, "index.html",
                                        {"error": "用户名或者密码错误"})


# 退出登录
def logout_view(request):
    logout(request)  # 清楚用户登录状态
    response = HttpResponseRedirect('/')
    return response




# 添加项目
@login_required
def add_project(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm()
    return render(request, 'project_manage.html', {'form': form})
