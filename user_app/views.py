from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from project_app.forms import LoginForm, LoginForm
from django.contrib.auth.models import User
# Create your views here.https://sobooks.cc/books/10313.html#respond

def index(request):
    return render(request, "Login.html")

#注册
def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/api/home/')
    elif request.method == "POST":
        username = request.POST.get("username", '')
        email = request.POST.get('email', '18630146437@mail.com')
        password2 = request.POST.get("password2", '')
        password3 = request.POST.get("password3", '')
        if password2 != password3:  # 判断两次密码是否相同
            return render(request, 'Login.html', {'message': '两次输入的密码不同！'})
        else:
            user = User.objects.create_user(username=username,
                                            email='18630146437@mail.com',
                                            is_staff=1,
                                            password=password2)
            user.save()
            return render(request, 'Login.html', {'message': '注册成功'})  # 自动跳转到登录页面

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
            return render(request, 'Login.html',{'user': user,
                                                'message': '用户名或密码错误！'})
    return render(request, 'Login.html', {'login_form': login_form})

#退出
def logout_view(request):
    logout(request)
    #清除cookie里保存的username
    return render(request, 'Login.html')
