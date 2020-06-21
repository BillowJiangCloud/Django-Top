from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    T_id = models.ForeignKey('TopInfo', on_delete=models.CASCADE, null=True, verbose_name='关联排行信息')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class TopInfo(models.Model):
    num = models.CharField(max_length=30, verbose_name='客户端号码', unique=True)
    score = models.IntegerField(default=0, verbose_name='分数')
    top = models.IntegerField(default=None, null=True, verbose_name='排名')
    time = models.DateTimeField(auto_now=True, verbose_name='最新修改时间')

    class Meta:
        verbose_name = '分数以及排行信息'
        verbose_name_plural = verbose_name
