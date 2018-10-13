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

class Module(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, default="")
    describe = models.TextField(default="")
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
