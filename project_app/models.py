from django.db import models

# Create your models here.
'''
name 项目名称
stats 状态
create_time 创建时间
remarks 备注
'''
class Project(models.Model):
    project_name = models.CharField(max_length=20)
    project_status = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)
    project_remarks = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name

'''
project 项目名称
name 模块名称
create_time 创建时间
describe 备注
'''
class Module(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=100)
    module_describe = models.TextField(max_length=100)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
