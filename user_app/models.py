from django.db import models

# Create your models here.
'''
name 项目名称
stats 状态
create_time 创建时间
remarks 备注
'''
class Project(models.Model):
    name = models.CharField(max_length=20)
    status = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)
    remarks = models.CharField(max_length=100)

    def __str__(self):
        return self.name
