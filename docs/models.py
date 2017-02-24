# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible



@python_2_unicode_compatible
class Docsdb(models.Model):
    doc_name = models.CharField(max_length=200)
    price = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.doc_name


@python_2_unicode_compatible
class Teambuildingdb(models.Model):
    choice_sex = ((u'f', u"女"), (u"m", u"男"), (u"x", u'双'))
    qa_name = models.CharField(max_length=200)
    sex = models.CharField(max_length=1, choices=choice_sex, default=u"x")
    go_where = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.qa_name

    class Meta:
        verbose_name = '团建信息'
        verbose_name_plural = '团建信息'
        ordering = ['id']  # 按照哪个栏目排序

