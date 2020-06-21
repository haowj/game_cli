from django.db import models

# Create your models here.

class ClientData(models.Model):
    user_name = models.CharField('客户端', max_length=256, unique=True, db_index=True, help_text='客户端')
    integral = models.IntegerField('积分', help_text='积分')
    update_time = models.DateTimeField('更新时间', auto_now=True, help_text='更新时间')
    create_time = models.DateTimeField('创建时间', auto_now_add=True, help_text='创建时间')