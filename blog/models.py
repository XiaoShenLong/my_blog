from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField(auto_now=True)
    #摘要
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ['-created_time']
    # on_delete
    # on_delete = None,  # 删除关联表中的数据时,当前表与其关联的field的行为
    # on_delete = models.CASCADE,  # 删除关联数据,与之关联也删除
    # on_delete = models.DO_NOTHING,  # 删除关联数据,什么也不做
    # on_delete = models.PROTECT,  # 删除关联数据,引发错误ProtectedError
    # # models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
    # on_delete = models.SET_NULL,  # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
    # # models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
    # on_delete = models.SET_DEFAULT,  # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
    # on_delete = models.SET,  # 删除关联数据,
    # a.与之关联的值设置为指定值, 设置：models.SET(值)
    # b.与之关联的值设置为可执行对象的返回值, 设置：models.SET(可执行对象)


