# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 00:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_project_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='photo',
            field=models.URLField(default='img/user_default.png'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='project',
            name='skills',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='projectusers',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Project'),
        ),
        migrations.AlterField(
            model_name='projectusers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
