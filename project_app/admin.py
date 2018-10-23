from django.contrib import admin
from project_app.models import Project, Module
# Register your models here.



class ProjectAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'project_name', 'create_time', 'project_status', 'project_remarks']
    search_fields = ['project_name']    #搜索栏
    list_filter = ['project_status']    #过滤器

class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'module_name', 'module_describe', 'create_time', 'project']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)
