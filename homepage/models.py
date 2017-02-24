# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Homepagedb(models.Model):
    halo_text = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.CharField(max_length=200)

    def __str__(self):
        return self.halo_text

        # 在Python3中使用 def __str__(self)
        # def __str__(self):
        #     return "this is Homepagedb.__str__"
@python_2_unicode_compatible
class Userdb(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.username