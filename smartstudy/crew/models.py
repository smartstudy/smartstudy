# -*- coding: utf-8 -*-
from django.db import models


class Crew(models.Model):
    class Meta:
        verbose_name = u'부족원'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    nick = models.CharField(verbose_name=u'별명',
                            help_text=u'모듈이 표시되는 한글 명칭을 적어주세요.',
                            max_length=50)
    uid = models.CharField(verbose_name=u'영문 아이디', max_length=50, null=True, blank=True)
    picture = models.ImageField(verbose_name=u'사진', upload_to='crew')
    comment = models.TextField(verbose_name=u'한마디',)
