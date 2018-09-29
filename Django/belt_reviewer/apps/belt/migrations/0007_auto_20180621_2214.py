# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-21 22:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0006_auto_20180621_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.RemoveField(
            model_name='review',
            name='book',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
