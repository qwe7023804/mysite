from django.contrib import admin
from user_app.models import Project
# Register your models here.



class ProjectAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name', 'create_time', 'status', 'remarks']
    search_fields = ['name']    #搜索栏
    list_filter = ['status']    #过滤器

admin.site.register(Project, ProjectAdmin)
