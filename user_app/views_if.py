from django.http import JsonResponse
from django.shortcuts import render
from user_app.models import Project
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from user_app import models


#添加创建项目接口
def add_project(request):
    if request.method == 'POST':
        eid = request.POST.get('eid', None)
        project_name = request.POST.get('prject_name', None)
        project_status = request.POST.get('project_status', True)
        #create_time = request.POST.get('create_time', None)
        project_remarks = request.POST.get('project_remarks', None)
        models.Project.objects.create(
                                        project_name = project_name,
                                        project_status = project_status,
                                        project_remarks = project_remarks
                                        )
        projekt_list = models.Project.objects.all()
        return HttpResponseRedirect('/home/')
    else:
        return render(request, 'Create_Project.html')


#项目查询接口
def get_project_list(request):
    eid = request.GET.get('eid', '')
    project_name = request.GET.get('project_name', '')
    project = {}
    print('project',project)
    project['project_name'] = result.project_name
    project['project_status'] = result.project_status
    project['create_time'] = result.create_time
    return rend(request, 'Create_Project.html', {'status':200, 'message':'success'})
