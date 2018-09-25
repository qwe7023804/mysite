from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login_action(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        if username =='' or password == '':
            return render(request, 'index.html', {'error': 'username or password is none'})
