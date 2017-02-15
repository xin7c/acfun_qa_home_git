from __future__ import unicode_literals
from django.db import models


class Homepagedb(models.Model):
    halo_text = models.CharField(max_length=200)
