# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-22 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0002_teambuildingdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='teambuildingdb',
            name='comments',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
