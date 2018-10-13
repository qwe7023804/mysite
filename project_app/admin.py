from django.contrib import admin
from project_app.models import Project
# Register your models here.



class ProjectAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'project_name', 'create_time', 'project_status', 'project_remarks']
    search_fields = ['project_name']    #搜索栏
    list_filter = ['project_status']    #过滤器

admin.site.register(Project, ProjectAdmin)
