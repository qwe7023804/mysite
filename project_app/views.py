from django.shortcuts import render
from project_app.models import Project
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from project_app import models
from django.utils import timezone
from project_app.forms import ProjectForm

#主页面
@login_required
def home(request):
    username = request.session.get('user', '')
    project_list = models.Project.objects.all()    #获取表所有信息
    return render(request, 'Home.html', {'username': username,
                                        'projects': project_list})
#创建项目页
@login_required
def create_project(request):
    eid = request.GET.get('id')
    username = request.session.get('user', '')
    time_now = timezone.now()
    return render(request, 'Project_Information.html', {'username': username,
                                                    'id': eid,
                                                    'time_now': time_now})

#添加创建项目接口
def add_project(request):
    create_form = ProjectForm(request.POST or None)
    if request.method == 'POST' and create_form.is_valid():
        project_name = create_form.cleaned_data.get('project_name')
        project_status = create_form.cleaned_data.get('project_status')
        project_remarks = create_form.cleaned_data.get('project_remarks')
        models.Project.objects.create(
                                        project_name = project_name,
                                        project_status = project_status,
                                        project_remarks = project_remarks
                                        )
        return HttpResponseRedirect('/api/home/')
    else:
        return render(request, 'Project_Information.html', {'error': '添加失败!!'})


#项目查询接口
def get_project_list(request):
    eid = request.GET.get('id')
    project = models.Project.objects.filter(id=eid)
    username = request.session.get('user', '')
    return render(request, 'Project_Information.html', {'status':200, 'message':'success',
                                                'id': eid,
                                                'username': username,
                                                'projects': project})


#修改接口
def edit_project(request):
    project_id = request.GET.get('id')
    edit_form = ProjectForm(request.POST or None)
    if request.method == 'POST' and edit_form.is_valid():
        project_name = edit_form.cleaned_data.get('project_name')
        project_status = edit_form.cleaned_data.get('project_status')
        project_remarks = edit_form.cleaned_data.get('project_remarks')
        print(project_id, project_name, project_remarks)
        models.Project.objects.filter(id = project_id).update(
                    project_name= project_name,
                    project_status= project_status,
                    project_remarks= project_remarks
                    )
        return HttpResponseRedirect('/api/home/')
    else:
        return HttpResponseRedirect('/api/get_project_list/?id={}'.format(project_id))



#删除项目
def delete_project(request):
    eid = request.GET.get('id')
    models.Project.objects.filter(id = eid).delete()
    return HttpResponseRedirect('/api/home/')
