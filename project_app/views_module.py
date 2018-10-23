from django.shortcuts import render
from project_app.models import Project, Module
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
#from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from project_app import models
from django.utils import timezone
from project_app.forms import ModuleForm

@login_required
def module(request):
    modules = models.Module.objects.all()
    return render(request, 'Module.html',
                            {'modules': modules})

@login_required
def create_module(request):
    projects = Project.objects.all()
    time_now = timezone.now()
    return render(request, 'Module_Information.html',
                            {'time_now': time_now,
                            'projects': projects})


#创建模块
@login_required
def add_module(request):
    if request.method == 'POST':
        create_form = ModuleForm(request.POST or None)
        print(create_form)
        if create_form.is_valid():
            project_name = create_form.cleaned_data.get['project_name']
            module_name = create_form.cleaned_data.get['module_name']
            module_describe = create_form.cleaned_data.get['describe']
            project_obj = Project.objects.get(project_name=project_name)
            models.Module.objects.create(module_name = module_name,
                                        module_describe = module_describe,
                                        project_id = int(project_obj.id)
                                        )
    return HttpResponseRedirect('/api/module/')
