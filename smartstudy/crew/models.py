# -*- coding: utf-8 -*-
from django.db import models


class Crew(models.Model):
    class Meta:
        verbose_name = u'부족원'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    nick = models.CharField(verbose_name=u'별명', max_length=50)
    name = models.CharField(verbose_name=u'이름', max_length=50,
                            null=True, blank=True)
    uid = models.CharField(verbose_name=u'영문 아이디', max_length=50,
                           null=True, blank=True)
    picture = models.ImageField(verbose_name=u'사진', upload_to='crew')
    comment = models.TextField(verbose_name=u'한마디', blank=True)
    email = models.EmailField(verbose_name=u'이메일',null=True, blank=True)
    home = models.URLField(verbose_name=u'홈페이지',null=True, blank=True)
    facebook = models.URLField(verbose_name=u'페이스북',null=True, blank=True)
    twitter = models.URLField(verbose_name=u'트위터',null=True, blank=True)
