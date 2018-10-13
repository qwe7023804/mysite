from django.shortcuts import render
from project_app.models import Project
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from project_app import models

#主页面
@login_required
def home(request):
    username = request.session.get('user', '')
    project_list = models.Project.objects.all()    #获取表所有信息
    return render(request, 'home.html', {'username': username,
                                        'projects': project_list})

#添加创建项目接口
def add_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name', None)
        project_status = request.POST.get('project_status', '')
        if project_status == 'on':
            project_status = 1
        else:
            project_status = 0
        project_remarks = request.POST.get('project_remarks', None)
        print(project_name, project_remarks)
        models.Project.objects.create(
                                        project_name = project_name,
                                        project_status = project_status,
                                        project_remarks = project_remarks
                                        )
        return HttpResponseRedirect('/api/home/')
    else:
        return render(request, 'Create_Project.html')


#项目查询接口
def get_project_list(request):
    eid = request.GET.get('id')
    project = models.Project.objects.filter(id=eid)
    username = request.session.get('user', '')
    return render(request, 'Edit_Project.html', {'status':200, 'message':'success',
                                                'username': username,
                                                'projects': project})


#修改接口
def edit_project(request):
    project_id = request.GET.get('id')
    project_name = request.POST.get('project_name', None)
    project_status = request.POST.get('project_status', 0)
    if project_status == 'on':
        project_status = 1
        print('1', project_status)
    else:
        project_status = 0
    project_remarks = request.POST.get('project_remarks', None)
    print(project_id, project_name, project_remarks)
    models.Project.objects.filter(id = project_id).update(
                    project_name= project_name,
                    project_status= project_status,
                    project_remarks= project_remarks
                    )
    return HttpResponseRedirect('/api/home/')



#删除项目
def delete_project(request):
    eid = request.GET.get('id')
    print(eid)
    models.Project.objects.filter(id = eid).delete()
    return HttpResponseRedirect('/api/home/')
