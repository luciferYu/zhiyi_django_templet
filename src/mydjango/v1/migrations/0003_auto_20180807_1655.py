# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_auto_20180807_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testparent',
            name='parent_childs',
        ),
        migrations.AddField(
            model_name='testchild',
            name='parent_childs',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='v1.TestParent'),
        ),
    ]