# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-21 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0002_auto_20180621_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]