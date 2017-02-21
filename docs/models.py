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